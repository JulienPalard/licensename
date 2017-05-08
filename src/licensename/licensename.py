#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module parses licenses files or text, and give back their name, like:

>>> print(licensename.from_file('./LICENSE'))
>>> 'mit'

or as a script:

$ licensename ./LICENSE
mit

"""

import argparse
import sys
import re


from unidecode import unidecode
from licensename import __version__
from licensename.known_licenses import LICENSE_TREE


__author__ = "Julien Palard"
__copyright__ = "Julien Palard"
__license__ = "mit"


SPACES = r'(?:[ \t\f\v\u00A0\u2028])'
UNORDERED_LIST = r'(?:[*\u2022+])'
ORDERED_LIST = r'(?:[0-9]\.)'
BULLET_MARKER = r'(?:{unordered}|{ordered})'.format(
    ordered=ORDERED_LIST,
    unordered=UNORDERED_LIST)
BULLET_ITEM = r'(?:{spaces}*{bullet_marker}{spaces}+)'.format(
    bullet_marker=BULLET_MARKER,
    spaces=SPACES)


def line_match_pattern(line, patterns):
    if isinstance(patterns, str):
        return patterns
    for pattern, subpatterns in patterns:
        if pattern in line:
            found = line_match_pattern(line, subpatterns)
            if found:
                return found


def canonicalize(license_text):
    simplified_text = license_text.lower()
    # Remove leading and trailing spaces:
    simplified_text = re.sub(r'^[ \t\f\v\xa0]+|[ \xA0\u2028\r\t\f\v]+$', '',
                             simplified_text, 0, re.M)
    # Remove lists prefixes:
    simplified_text = re.sub('^[0-9*.+-]* +', '', simplified_text, 0, re.M)
    # Deduplicate spaces:
    simplified_text = re.sub(r'\s+', ' ', simplified_text, 0, re.M)
    # Replace unicode quotation marks by ascii ones
    simplified_text = unidecode(simplified_text)
    # Deduplicate double quotes (thanks Microsoft):
    simplified_text = simplified_text.replace('""', '"')
    return simplified_text


def from_lines(license_lines):
    """Parse a license text, returns a license name.
    """
    current_patterns = LICENSE_TREE
    for line in license_lines:
        if not line:
            continue
        remaining_patterns = line_match_pattern(line, current_patterns)
        if remaining_patterns:
            current_patterns = remaining_patterns
            if isinstance(current_patterns, str):
                return current_patterns


def from_text(license_text):
    """Parse a license text, returns a license name.
    """
    return from_lines(canonicalize(license_text).split('\n'))


def from_file(license_path):
    """Parse a license file, returns a license name.
    """
    with open(license_path) as license_file:
        return from_text(license_file.read().strip())


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Find name of a given license file.")
    parser.add_argument(
        '--version',
        action='version',
        version='licensename {ver}'.format(ver=__version__))
    parser.add_argument(
        '--pretty-print',
        action='store_true',
        help="Pretty print license file.")
    parser.add_argument(
        dest="license_path",
        help="Path of a license file",
        metavar="LICENSE")
    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    if args.pretty_print:
        with open(args.license_path) as license_file:
            print(canonicalize(license_file.read()))
            return
    print(from_file(args.license_path))


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
