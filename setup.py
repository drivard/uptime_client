#!/usr/bin/env python

from setuptools import setup, find_packages
from uptime.__init__ import __version__ as VERSION

setup(
    name="Uptime Client",

    version=VERSION,

    description='''Python command line tool to return the uptime of
    your system to the uptime-website.''',

    author="Dominick Rivard",

    author_email="dominick.rivard@gmail.com",

    maintainer="Dominick Rivard",

    license="GPL3",

    url="https://github.com/drivard/uptime_client",

    package_dir={"uptime_client": "uptime_client"},

    zip_safe=True,

    install_requires=["", ],

    entry_points={
        "console_scripts": [
            "uptimz = uptime_client.cli:main",
        ]},

    keywords="uptime linux",

    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: ",
        "License :: ",
        "Programming Language :: Python",
        "Topic :: ",
    ],
)
