#!/usr/bin/env python3
"""
Regenerate Sinkholes_List in every supported format from the authoritative
CSV.

Inputs
------
Sinkholes_List.csv is the single source of truth. Every other format is
derived from it on each run.

Outputs
-------
Sinkholes_List.json, Sinkholes_List.xlsx, Sinkholes_List.ods, and the
Markdown table embedded in README.md (when --readme is passed) are rewritten.

Modes
-----
  python add_rows.py            Append rows from addition.py, then regenerate.
  python add_rows.py --sync     Skip addition.py, just regenerate from CSV.
  python add_rows.py --validate Run schema and IP validation, exit non-zero
                                on any failure. Combine with other flags.
  python add_rows.py --readme   Also rewrite the table block in README.md.
  python add_rows.py --debug    Print rows to stdout, write nothing.

Original author: Spencer Walden (Masq), 2018.
2026 refresh: replaced the pyexcel pipeline with stdlib + openpyxl + odfpy
so the script runs on current Python releases that lack pyexcel wheels.
"""

from __future__ import annotations

import argparse
import csv
import ipaddress
import json
import re
import sys
from pathlib import Path

OUTFILE_BASE = "Sinkholes_List"
HEADER = ("Organization", "IP Range", "Whois", "Notes")

README_PATH = Path("README.md")
TABLE_START = "<!-- sinkholes-table:start -->"
TABLE_END = "<!-- sinkholes-table:end -->"

# Inclusive last-octet range like "192.168.0.1-10" or "192.168.0.1-12".
RANGE_RE = re.compile(r"^(\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d{1,3})-(\d{1,3})$")


def validate_row(row: dict, line_no: int) -> list[str]:
    """Return a list of human-readable problems for this row. Empty if OK."""
    problems: list[str] = []
    for key in HEADER:
        if key not in row:
            problems.append(f"line {line_no}: missing column {key!r}")
    if problems:
        return problems

    if not row["Organization"].strip():
        problems.append(f"line {line_no}: Organization is empty")
    ip_value = row["IP Range"].strip()
    if not ip_value:
        problems.append(f"line {line_no}: IP Range is empty")
    else:
        problems.extend(_validate_ip_field(ip_value, line_no))
    return problems


def _validate_ip_field(value: str, line_no: int) -> list[str]:
    """Validate the IP Range cell. Allow single IP, CIDR, or short range."""
    # CIDR or single IP, parsed by ipaddress.
    try:
        ipaddress.ip_network(value, strict=False)
        return []
    except ValueError:
        pass

    match = RANGE_RE.match(value)
    if match:
        prefix, low_s, high_s = match.groups()
        low, high = int(low_s), int(high_s)
        try:
            ipaddress.ip_address(f"{prefix}.{low}")
            ipaddress.ip_address(f"{prefix}.{high}")
        except ValueError as err:
            return [f"line {line_no}: invalid IP range {value!r}: {err}"]
        if low > high:
            return [f"line {line_no}: IP range {value!r} is reversed"]
        return []

    return [f"line {line_no}: cannot parse IP Range {value!r}"]


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != list(HEADER):
            raise ValueError(
                f"unexpected CSV header in {path}: {reader.fieldnames!r}"
            )
        return [dict(row) for row in reader]


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def write_xlsx(path: Path, rows: list[dict]) -> None:
    try:
        from openpyxl import Workbook
    except ImportError:
        print("[!] openpyxl not installed, skipping .xlsx output")
        return
    wb = Workbook()
    ws = wb.active
    ws.title = "Sinkholes"
    ws.append(list(HEADER))
    for row in rows:
        ws.append([row[col] for col in HEADER])
    wb.save(path)


def write_ods(path: Path, rows: list[dict]) -> None:
    try:
        from odf.opendocument import OpenDocumentSpreadsheet
        from odf.table import Table, TableCell, TableRow
        from odf.text import P
    except ImportError:
        print("[!] odfpy not installed, skipping .ods output")
        return
    doc = OpenDocumentSpreadsheet()
    table = Table(name="Sinkholes")
    header_row = TableRow()
    for col in HEADER:
        cell = TableCell()
        cell.addElement(P(text=col))
        header_row.addElement(cell)
    table.addElement(header_row)
    for row in rows:
        tr = TableRow()
        for col in HEADER:
            cell = TableCell()
            cell.addElement(P(text=row[col]))
            tr.addElement(cell)
        table.addElement(tr)
    doc.spreadsheet.addElement(table)
    doc.save(path)


def render_markdown_table(rows: list[dict]) -> str:
    """Return a GitHub-flavored Markdown table for the rows."""
    widths = {col: len(col) for col in HEADER}
    for row in rows:
        for col in HEADER:
            widths[col] = max(widths[col], len(str(row.get(col, ""))))

    def fmt_row(values: list[str]) -> str:
        cells = [v.ljust(widths[col]) for v, col in zip(values, HEADER)]
        return "| " + " | ".join(cells) + " |"

    lines = [
        fmt_row(list(HEADER)),
        "| " + " | ".join("-" * widths[col] for col in HEADER) + " |",
    ]
    for row in rows:
        lines.append(fmt_row([str(row.get(col, "")) for col in HEADER]))
    return "\n".join(lines) + "\n"


def update_readme(rows: list[dict]) -> bool:
    if not README_PATH.exists():
        print(f"[!] {README_PATH} not found, skipping README update")
        return False
    text = README_PATH.read_text(encoding="utf-8")
    if TABLE_START not in text or TABLE_END not in text:
        print(
            f"[!] {README_PATH} is missing the table markers "
            f"{TABLE_START!r} / {TABLE_END!r}, skipping README update"
        )
        return False
    table = render_markdown_table(rows)
    pattern = re.compile(
        re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END),
        re.DOTALL,
    )
    new_text = pattern.sub(
        TABLE_START + "\n\n" + table + "\n" + TABLE_END,
        text,
    )
    if new_text != text:
        README_PATH.write_text(new_text, encoding="utf-8")
        print(f"[+] Updated table block in {README_PATH}")
    else:
        print(f"[=] Table block in {README_PATH} already up to date")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    ap.add_argument(
        "--debug", action="store_true",
        help="Print rows and exit; write nothing.",
    )
    ap.add_argument(
        "--sync", action="store_true",
        help="Skip addition.py, just regenerate output formats from the CSV.",
    )
    ap.add_argument(
        "--validate", action="store_true",
        help="Validate every row and exit non-zero on any failure.",
    )
    ap.add_argument(
        "--readme", action="store_true",
        help="Also rewrite the table block inside README.md.",
    )
    args = ap.parse_args()

    csv_path = Path(f"{OUTFILE_BASE}.csv")
    try:
        rows = read_csv(csv_path)
    except (OSError, ValueError) as err:
        print(f"[-] Failed to read {csv_path}: {err}")
        return 1

    if not args.sync:
        try:
            from addition import addition as new_rows
        except ImportError as err:
            print(f"[-] Could not import addition.py: {err}")
            return 1
        for new_row in new_rows:
            normalized = {col: str(new_row.get(col, "")).strip() for col in HEADER}
            rows.append(normalized)

    if args.validate:
        problems: list[str] = []
        for idx, row in enumerate(rows, start=2):  # data starts at line 2
            problems.extend(validate_row(row, idx))
        if problems:
            print("[-] Validation failed:")
            for problem in problems:
                print(f"    {problem}")
            return 2
        print(f"[+] Validation passed: {len(rows)} rows")

    if args.debug:
        from pprint import pprint
        pprint(rows)
        return 0

    write_csv(csv_path, rows)
    print(f"[+] Wrote {csv_path} ({len(rows)} rows)")

    write_json(Path(f"{OUTFILE_BASE}.json"), rows)
    print(f"[+] Wrote {OUTFILE_BASE}.json")

    write_xlsx(Path(f"{OUTFILE_BASE}.xlsx"), rows)
    print(f"[+] Wrote {OUTFILE_BASE}.xlsx")

    write_ods(Path(f"{OUTFILE_BASE}.ods"), rows)
    print(f"[+] Wrote {OUTFILE_BASE}.ods")

    if args.readme:
        update_readme(rows)

    return 0


if __name__ == "__main__":
    sys.exit(main())
