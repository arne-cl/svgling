#!/usr/bin/env python

from __future__ import with_statement
from __future__ import absolute_import
from io import open
try:
    from setuptools import setup
except:
    from distutils.core import setup

with open(u"README.md", u"r") as fh:
    long_description = fh.read()

setup(name=u'svgling',
    version=u'0.3.0',
    description=u'SVG+Python based rendering of linguistics-style (constituent) trees',
    long_description=long_description,
    long_description_content_type=u"text/markdown",
    author=u'Kyle Rawlins',
    author_email=u'kgr@jhu.edu',
    license=u'MIT',
    url=u'https://github.com/rawlins/svgling',
    # svgwrite 1.3.1 is the last version to support Python 2
    install_requires=['svgwrite==1.3.1', 'pyparsing==2.4.7'],
    python_requires=u'==2.7.*',
    packages=[u'svgling'],
    classifiers=[
        u"Development Status :: 4 - Beta",
        u"License :: OSI Approved :: MIT License",
        u"Intended Audience :: Science/Research",
        u"Topic :: Multimedia :: Graphics",
        u"Topic :: Scientific/Engineering :: Visualization",
        u"Topic :: Text Processing :: Linguistic",
        u"Topic :: Text Processing :: Markup",
        u"Topic :: Utilities",
        u"Framework :: Jupyter",
        u"Environment :: Web Environment"]
    )
