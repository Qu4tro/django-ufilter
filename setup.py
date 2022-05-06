#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

from setuptools import find_packages, setup

from django_ufilter import __author__, __version__


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), "rb") as fid:
        return fid.read().decode("utf-8")


authors = read("AUTHORS.rst")
history = read("HISTORY.rst").replace(".. :changelog:", "")
licence = read("LICENSE.rst")
readme = read("README.rst")

req = read("requirements.txt").splitlines()

requirements = req + ["setuptools"]

description = " - ".join(
    [
        "Django UFilter provides a safe way to filter data via human-friendly URLs",
        "A fork from django-url-filter",
    ]
)

setup(
    name="django-ufilter",
    version=__version__,
    author=__author__,
    description=description,
    long_description="\n\n".join([readme, history, authors, licence]),
    url="https://github.com/miki725/django-url-filter",
    license="MIT",
    packages=find_packages(exclude=["test_project*", "tests*"]),
    install_requires=requirements,
    keywords=" ".join(["django django-rest-framework"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Development Status :: 2 - Pre-Alpha",
    ],
)
