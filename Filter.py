#!/usr/bin/env python3

import argparse
import copy
import string
import itertools

MICROSOFT_SYMBOLS = r'~!@#$%^&*_-+=`|\(){}[]:;"<>,.?/' + "'"


def is_complex(word: str) -> bool:
    has_lower = False
    has_upper = False
    has_symbol = False
    has_digit = False

    for letter in word:
        if letter in string.ascii_lowercase:
            has_lower = True
        elif letter in string.ascii_uppercase:
            has_upper = True
        elif letter in string.digits:
            has_digit = True
        elif letter in MICROSOFT_SYMBOLS:
            has_symbol = True

    count = 0
    for b in has_lower, has_upper, has_symbol, has_digit:
        if b:
            count += 1

    return count >= 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--complexity',
                        action='store_true',
                        help='Filter with Microsoft complexity filter (does not affect minimum length)')
    parser.add_argument('-m', '--min-length', type=int, help='Minimum length')
    parser.add_argument('--max-length', type=int, help='Maximum length')
    parser.add_argument('-w', '--word', nargs='+', help='Wordlist on command line')
    parser.add_argument('-s', '--sort', action='store_true', help='Sort unique')
    parser.add_argument('-t', '--top', type=int, help='Take the top X words')
    parser.add_argument('file', nargs='+', help='Wordlist file')
    args = parser.parse_args()

    words = iter([])
    file_handles = []
    for file in args.file:
        fp = open(file, encoding='iso-8859-1')
        file_handles.append(fp)
        words = itertools.chain(words, (line.strip() for line in fp))

    if args.word:
        words = itertools.chain(words, args.word)

    if args.sort:
        words = sorted(set(words))

    count = 0
    for word in words:
        if args.complexity and not is_complex(word):
            continue

        if args.min_length and len(word) < args.min_length:
            continue

        if args.max_length and len(word) > args.max_length:
            continue

        count += 1
        print(word)

        if args.top and count > args.top:
            break


if __name__ == '__main__':
    main()
