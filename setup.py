#!/usr/bin/env python3
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(install_requires=required, packages=['bibtools'])
