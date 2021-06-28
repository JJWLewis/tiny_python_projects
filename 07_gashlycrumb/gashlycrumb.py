#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Return letter description from input file"""

    args = get_args()
    
    file_dict:dict = {}

    # Create dict from file
    file_dict = {line[0].upper(): line.rstrip() for line in args.file}
    
    for letter in args.letter:
        print(file_dict.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
