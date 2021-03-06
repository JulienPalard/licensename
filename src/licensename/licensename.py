#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module parses licenses files or text, and give back their name, like:

>>> print(licensename.from_file('./LICENSE'))
>>> 'mit'

or as a script:

$ licensename ./LICENSE
mit

"""

import re
import sys
import logging

from unidecode import unidecode
from licensename import __version__
from licensename.known_licenses import LICENSE_TREE


__author__ = "Julien Palard"
__copyright__ = "Julien Palard"
__license__ = "mit"
logger = logging.getLogger(__name__)


def line_match_pattern(line, patterns):
    if isinstance(patterns, str):
        return patterns
    for pattern, subpatterns in patterns:
        if pattern in line:
            logger.info("Matched: %s", repr(pattern))
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


def from_text(license_text):
    """Parse a license text, returns a license name.
    """
    return line_match_pattern(canonicalize(license_text), LICENSE_TREE)


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
    import argparse
    parser = argparse.ArgumentParser(
        description="Find name of a given license file.")
    parser.add_argument(
        '--version',
        action='version',
        version='licensename {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        dest="license_path",
        help="Path of a license file",
        metavar="LICENSE")
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    print(from_file(args.license_path))


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
