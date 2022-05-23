#!/usr/bin/env python3

from setuptools import find_packages, setup

from pathlib import Path

setup(
	name="Lindex",
	packages=find_packages(include=["Indexing"]),
	version="1.0.0",
	description="A Python Library for Interacting With Databases",
	author="@some1and2",
	author_email='04x0xx@gmail.com',
	license="GPL-3.0",
	install_requires=["Lindex == 1.0.1"],
	setup_requires=[],
	long_description = ( Path(__file__).parent / "README.md" ).read_text(),
	long_description_content_type='text/markdown'
)
