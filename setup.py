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
    install_requires=u'svgwrite',
    python_requires=u'>=3',
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
