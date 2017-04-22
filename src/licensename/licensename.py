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


def unwrap(text):
    """Kind of undoing a textwrap.wrap() on every paragraphs.

    Also split:

    - Lists, as if every item was a paragraph.
    - Phrases ending a line, as if it's the end of a paragraph, even
      if there is no blank line after it.

    """
    spaces = r'(?:[ \t\f\v\u00A0\u2028])'
    unordered_list = r'(?:[*\u2022])'
    ordered_list = r'(?:[0-9]\.)'
    bullet_marker = r'(?:{unordered}|{ordered})'.format(
        ordered=ordered_list,
        unordered=unordered_list)
    bullet_item = r'(?:(?<=\n){spaces}*{bullet_marker}{spaces}+)'.format(
        bullet_marker=bullet_marker,
        spaces=spaces)
    text_paragraph_separator = '(?:\n{spaces}*\n+)'.format(spaces=spaces)
    line_ending_with_a_dot = r'(?:(?<=\.)\n)'
    paragraph_separator = '{}|{}|{}'.format(
        bullet_item,
        text_paragraph_separator,
        line_ending_with_a_dot
    )
    return '\n\n'.join(line.replace('\n', ' ') for line in
                       re.split(paragraph_separator, text, 0) if line)


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


def canonicalize(license_text):
    simplified_text = remove_useless_lines(license_text)
    unwrapped_text = unwrap(simplified_text)
    # Remove leading and trailing spaces:
    unwrapped_text = re.sub(r'^[ \t\f\v\xa0]+|[ \xA0\u2028\r\t\f\v]+$', '', unwrapped_text, 0, re.M)
    # Remove lists prefixes:
    unwrapped_text = re.sub('^[0-9*.-]* ', '', unwrapped_text, 0, re.M)
    # Deduplicate spaces:
    unwrapped_text = re.sub('[ \\t\xA0\u2028]+', ' ', unwrapped_text, 0, re.M)

    return unwrapped_text


def from_lines(license_lines):
    """Parse a license text, returns a license name.
    """
    current_patterns = KNOWN_FIRST_LINES
    for line in license_lines:
        if not line:
            continue
        found_line = line_match_pattern(line, current_patterns)
        if found_line:
            current_patterns = current_patterns[found_line]
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
        description="Just a Fibonnaci demonstration")
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
