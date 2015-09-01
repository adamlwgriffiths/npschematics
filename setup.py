#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from npschematics import __version__

setup(
    name='npschematics',
    license='BSD',
    version=__version__,
    description='Numpy Types for Schematics',
    author=u'Adam Griffiths',
    url='http://github.com/adamlwgriffiths/npschematics',
    requires = ['schematics', 'numpy'],
    packages=['npschematics'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
