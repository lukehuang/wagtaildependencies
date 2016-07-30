from __future__ import absolute_import, print_function, unicode_literals
import datetime
import subprocess
from codecs import open
from os import path
from setuptools import find_packages, setup
from wagtaildependencies import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wagtaildependencies',
    version=__version__,
    description='Makes it easy to manage front-end dependencies for Wagtail admin plugins',
    long_description=long_description,
    url='https://github.com/alexgleason/wagtaildependencies',
    author='Alex Gleason',
    author_email='alex@alexgleason.me',
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wagtail>=1.4.0",
        "Django>=1.7.1",
    ],
)
