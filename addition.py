#!/usr/bin/env python3
"""
Optional helper used by add_rows.py.

Define new rows in the `addition` list below. Each row is a dict with the
keys: Organization, IP Range, Whois, Notes.

When you run `python add_rows.py` (without --sync), every dict in this list
is appended to Sinkholes_List.csv before all output formats are regenerated.
The list may be left empty for routine regeneration; in that case prefer
`python add_rows.py --sync`.

IP Range accepts:
- Single IP: 192.168.0.1
- CIDR:      192.168.0.0/24
- Inclusive small range with shared first three octets: 192.168.0.1-10
"""

addition = [
    # {
    #     'Organization': '',
    #     'IP Range': '',
    #     'Whois': '',
    #     'Notes': '',
    # },
]
