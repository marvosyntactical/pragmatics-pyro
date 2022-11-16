#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

with open("requirements.txt", encoding="utf-8") as req_fp:
    install_requires = req_fp.readlines()

setup(
    name='pyro_rsa_book_utils',
    version='0.9.1',
    description='Pyro port of Problang.org',
    author='Marvin Koss',
    url='https://github.com/marvosyntactical/pragmatics-pyro',
    license='Apache License',
    install_requires=install_requires,
    packages=find_packages(exclude=[]),
    python_requires='>=3.10',
    project_urls={
        'Source': 'https://github.com/marvosyntactical/pragmatics-pyro',
    },
    entry_points={
        'console_scripts': [
        ],
    }
)

