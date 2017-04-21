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


from licensename import __version__
from licensename.known_licenses import KNOWN_FIRST_LINES


__author__ = "Julien Palard"
__copyright__ = "Julien Palard"
__license__ = "mit"


def simplify_line(line):
    line = line.strip()
    line = re.sub('^[0-9*.-]* ', '', line)
    line = re.sub(r'\s+', ' ', line)
    return line


def unwrap(text):
    return [paragraph.replace('\n', ' ') for paragraph in text.split('\n\n')]


def line_match_pattern(line, patterns):
    if line in patterns:
        return line
    for potential_regex in patterns:
        if '.*' not in potential_regex:
            continue
        if re.match(potential_regex, line):
            return potential_regex


def remove_useless_lines(license_text):
    license_text = license_text.split('\n')
    license_lines = [line for line in license_text if
                     not line.startswith('Copyright') and
                     not line.startswith('All rights reserved.') and
                     '(c)' not in line and
                     '(C)' not in line]
    return '\n'.join(license_lines)


def from_lines(license_lines):
    """Parse a license text, returns a license name.
    """
    current_patterns = KNOWN_FIRST_LINES
    for line in license_lines:
        if not line:
            continue
        found_line = line_match_pattern(line, current_patterns)
        if found_line is not None:
            current_patterns = current_patterns[found_line]
            if isinstance(current_patterns, str):
                return current_patterns


def from_text(license_text):
    """Parse a license text, returns a license name.
    """
    license_text = remove_useless_lines(license_text)
    license_lines = [simplify_line(line) for line in unwrap(license_text)]
    found = from_lines(license_lines)
    if found:
        return found
    license_lines = [simplify_line(line) for line in license_text.split('\n')]
    return from_lines(license_lines)


def from_file(license_path):
    """Parse a license file, returns a license name.
    """
    with open(license_path) as license_file:
        return from_text(license_file.read())


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a Fibonnaci demonstration")
    parser.add_argument(
        '--version',
        action='version',
        version='licensename {ver}'.format(ver=__version__))
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
    print(from_file(args.license_path))


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
