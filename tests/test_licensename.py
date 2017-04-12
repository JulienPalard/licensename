#!/usr/bin/env python3

import os
import glob
import pytest
from licensename.licensename import from_file

__author__ = "Julien Palard"
__copyright__ = "Julien Palard"
__license__ = "mit"


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'licenses/',
)


def test_files():
    assert list(glob.glob(os.path.join(FIXTURE_DIR, '*.txt')))
    for license_file in glob.glob(os.path.join(FIXTURE_DIR, '*.txt')):
        expected_license_name = os.path.basename(license_file.replace('.txt', ''))
        assert from_file(license_file) == expected_license_name
