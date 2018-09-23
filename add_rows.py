#!/usr/bin/env python3
"""
    Script to easy add rows to the sinkhole list! :D
"""

import sys
import json
from collections import OrderedDict
import csv

# This (in conjunction with plugins) allows us to convert to many formats
# namely, xls, xlsx, and ods
import pyexcel

# import our additional data
from addition import addition as our_additional_rows

# Our outfile name(s)
OUTFILE_NAME = 'Sinkholes_List'
HEADER = (
    'Organization',
    'IP Range',
    'Whois',
    'Notes'
)


def main(debug=False, sync=False):
    """
        Adds in additional entries to the Sinkhole List.
    """
    # just read from the json file since it's easiest
    infile = OUTFILE_NAME + '.csv'

    # list of supported extensions we want to write out to
    out_extensions = [
        'json',
        'csv',
        # let's do csv file first since it's easiest, and then just
        # copy things to other file formats
        'xls',
        'xlsx',
        'ods',
    ]

    try:
        with open(infile, 'r') as infile_handle:
            sinkholes = [row for row in csv.DictReader(infile_handle)]
    except Exception as error:
        print('[-] ERROR: {}'.format(error))
        sys.exit(1)

    # With the sync option, we don't want to add anything, just make sure every
    # file format is properly synced up with each other
    if not sync:
        sinkholes += our_additional_rows

    if debug:
        from pprint import pprint
        pprint(sinkholes)
    else:
        for extension in out_extensions:
            try:
                outfile_name = '{}.{}'.format(OUTFILE_NAME, extension)
                with open(outfile_name, 'w') as outfile_handle:
                    write_out(
                        our_data=sinkholes, 
                        to=outfile_handle,
                        with_filetype=extension, 
                        full_file_name=outfile_name
                    )
            except Exception as warning:
                # If we encountered an error with a certain format, just move
                # on...
                print('[!] Warning with {}: {}'.format(extension, warning))
                continue
            else:
                print('[+] Successfully wrote out to {}'.format(outfile_name))

    return True


def write_out(our_data, with_filetype, to=None, full_file_name=None):
    """
        Gets the text to write out for a given file extension with the given
        data.
    """
    sinkhole_list = our_data
    extension = with_filetype

    # Handle JSON files
    if extension == 'json':
        to.write(json.dumps(sinkhole_list))

    # Handle CSV files
    elif extension == 'csv':
        # First element keys should be the same consistent keys used throughout
        header = HEADER
        csv_out = csv.DictWriter(to, fieldnames=header)
        csv_out.writeheader()
        csv_out.writerows(sinkhole_list)

    elif extension in ['xlsx', 'xls', 'ods']:
        # Kinda cheating here... Just grab the CSV file we already wrote out
        # and copy it over to a different format
        csv_name = full_file_name.replace(extension, 'csv')
        pyexcel.save_as(file_name=csv_name, dest_file_name=full_file_name)

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
    ap.add_argument('--sync', action='store_true', help=(
        'Sync will simply *not* perform any adding of rows to files. Instead, '
        'it will perform all of the same actions to sync the files so each '
        'file format reflects the same data.'
    ))
    args = ap.parse_args()
    main(debug=args.debug, sync=args.sync)
