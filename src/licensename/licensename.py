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

from licensename import __version__
from licensename.known_licenses import KNOWN_FIRST_LINES


__author__ = "Julien Palard"
__copyright__ = "Julien Palard"
__license__ = "mit"


def from_text(license_text):
    """Parse a license text, returns a license name.
    """
    license_lines = license_text.split('\n')
    license_lines = [line.strip() for line in license_lines]
    license_lines = [line for line in license_lines if
                     line and
                     not line.startswith('Copyright') and
                     '(c)' not in line and
                     '(C)' not in line]
    current_line = 0
    current_patterns = KNOWN_FIRST_LINES
    while license_lines[current_line] in current_patterns:
        current_patterns = current_patterns[license_lines[current_line]]
        if isinstance(current_patterns, str):
            return current_patterns
        current_line += 1


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
