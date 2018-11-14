# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='searchlet',
    version='1.0.0',
    description='Python Search Algorithms',
    long_description=readme,
    author='David Chan',
    author_email='davidchan@berkeley.edu',
    url='https://github.com/DavidMChan/searchlet',
    license=license,
    install_requires=[
        'pytest >= 3.7.0',
    ],
    packages=find_packages(),  # exclude=('tests', 'docs')
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
