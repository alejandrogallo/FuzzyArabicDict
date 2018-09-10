# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as fd:
    long_description = fd.read()

setup(
    name='papis-scihub',
    version='1.2.0',
    author='FuzzyArabicDict team',
    maintainer='Alejandro Gallo',
    maintainer_email='aamsgallo@gmail.com',
    license='GPLv3',
    url='https://github.com/alejandrogallo/FuzzyArabicDict',
    install_requires=[
        'six',
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    description='A python based offline arabic dictionary',
    long_description=long_description,
    keywords=[
        'arabic', 'dictionary', 'cli'
    ],
    platforms=['linux', 'osx'],
)
