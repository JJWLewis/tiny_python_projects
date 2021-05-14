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
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='The number of insults',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-a',
                        '--adjectives',
                        help='The number of adjectives',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-s',
                        '--seed',
                        help='The random seed value',
                        metavar='int',
                        type=int,
                        default=1)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
