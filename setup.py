#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
    name = 'microblog',
    version='0.2.0',
    license='GNU General Public License v3',
    author='Rebu Thomas',
    author_email='rebumthomas@gmail.com',
    description='Microblog application for Flask',
    packages=['app'],
    platforms='any',
    install_requires=[
        'flask',
    ],
)