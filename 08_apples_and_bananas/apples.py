#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sentence',
                        metavar='sentence',
                        help='Either a string or file path')

    parser.add_argument('-v',
                        '--vowel',
                        help='vowel of choice to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.sentence):
        args.sentence = open(args.sentence, 'rt').read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel: str = args.vowel

    out_text: str = map(
        lambda cha: vowel
        if cha in 'aeiou' else vowel.upper()
        if cha in 'AEIOU' else cha,
        args.sentence
    )

    print(''.join(out_text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
