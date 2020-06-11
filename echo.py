#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "chrisescobeo0617"


import sys
import argparse


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument(
        'text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo"""
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    string_ = ns.text

    if ns.title:
        print(string_.title())
    elif ns.lower:
        print(string_.lower())
    elif ns.upper:
        print(string_.upper())
    else:
        print(string_)
    


if __name__ == '__main__':
    main(sys.argv[1:])
