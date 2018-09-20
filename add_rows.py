#!/usr/bin/env python3
"""
    Script to easy add rows to the sinkhole list! :D
"""

import sys
import json
import csv
# import xlsxwriter
# xls files: TODO
# import odswriter

# import our additional data
import addition

# Our outfile name(s)
OUTFILE_NAME = 'Sinkholes_List'


def main(debug = False):
    """
        Adds in additional entries to the Sinkhole List.
    """
    # just read from the json file since it's easiest
    infile = OUTFILE_NAME + '.json'

    # list of supported extensions we want to write out to
    out_extensions = [
        #'json',
        'xls',
        'xlsx',
        'ods',
        'csv'
    ]

    try:
        with open(infile, 'r') as infile:
            sinkholes = json.loads(infile.read())
    except Exception as error:
        print('[-] ERROR: {}'.format(error))
        sys.exit(1)

    sinkholes += addition.addition

    if debug:
        from pprint import pprint
        pprint(sinkholes)
    else:
        for extension in out_extensions:
            try:
                outfile_name = '{}.{}'.format(OUTFILE_NAME, extension)
                with open(outfile_name, 'w') as outfile_handle:
                    write_out(sinkholes, extension, to=outfile_handle)
            except Exception as warning:
                # If we encountered an error with a certain format, just move
                # on...
                print('[!] Warning with {}: {}'.format(extension, warning))
                continue
            else:
                print('[+] Successfully wrote out to {}'.format(outfile_name))

    return True


def write_out(sinkhole_dict, extension, to=None):
    """
        Gets the text to write out for a given file extension with the given
        data.
    """
    # Handle JSON files
    if extension == 'json':
        to.write(json.dumps(sinkhole_dict))

    # Handle CSV files
    elif extension == 'csv':
        # First element keys should be the same consistent keys used throughout
        header = list(sinkhole_dict[0].keys())
        csv_out = csv.DictWriter(to, fieldnames=header)
        csv_out.writeheader()
        csv_out.writerows(sinkhole_dict)

    # We got a weird extension or don't currently support it...
    else:
        raise NotImplementedError((
            'There is currently no implementation for writing out to {} '
            'files.'
        ).format(
            extension
        ))


if __name__ == '__main__':
    # If run from the command line vs imported from another python script
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--debug', action='store_true', help=(
        'A debug flag; will not write out to file '
        'will only print to stdout using pretty print'
    ))
    args = ap.parse_args()
    main(debug=args.debug)
