#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for licensename.

    This file was generated with PyScaffold 2.5.7, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup, find_packages


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=sphinx,
          package_dir={'': 'src'},
          packages=find_packages('src'))


if __name__ == "__main__":
    setup_package()
