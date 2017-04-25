#!/usr/bin/env python3

import os
import re
import glob
import pytest
from licensename.licensename import from_file, unwrap

__author__ = "Julien Palard"
__copyright__ = "Julien Palard"
__license__ = "mit"


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'licenses/',
)


@pytest.mark.parametrize(
    "license_file,license_name",
    [(license_file,
      os.path.basename(
          re.sub(r'(~[0-9]+)?\.txt', '', license_file))) for
     license_file in
     glob.glob(os.path.join(FIXTURE_DIR, '*.txt'))])
def test_files(license_file, license_name):
    assert from_file(license_file) == license_name
