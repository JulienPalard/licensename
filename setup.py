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


with open('README.rst') as readme_file:
    readme = readme_file.read()


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(
        name='licensename',
        version='0.4.1',
        description='Find a license name from a license file.',
        long_description=readme,
        author='Julien Palard',
        author_email='julien@palard.fr',
        license="MIT",
        url='https://github.com/JulienPalard/licensename',
        entry_points={
            'console_scripts': [
                 'licensename=licensename.licensename:run'
            ]
        },
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
        ],
        setup_requires=sphinx,
        package_dir={'': 'src'},
        install_requires=['textunwrap'],
        packages=find_packages('src'))


if __name__ == "__main__":
    setup_package()
