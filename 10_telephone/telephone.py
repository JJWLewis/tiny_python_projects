#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Telephone!
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Either string or path to file')

    parser.add_argument('-m',
                        '--mutations',
                        help="""floating point number between 0 and 1 that
                        represents a percentage of mutations to introduce""",
                        metavar='float',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text
    num_mutations = round(args.mutations * len(text))
    # Set seed (Default None is accepted)
    random.seed(args.seed)

    all_chars: str = ''.join(sorted(string.ascii_letters + string.punctuation))  # noqa: E999, E501

    # Deterministic random choice. Find indexes to change
    indexes = random.sample(range(len(text)), k=num_mutations)
    for i in indexes:
        random_char = random.choice(all_chars.replace(text[i], ''))  # Replace pops
        text = text[:i] + random_char + text[i+1:]

    print(f'You said: "{args.text}"\nI heard : "{text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
