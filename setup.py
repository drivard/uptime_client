#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "uptime_client",

    version = "0.1",

    description="""
        Python command line tool to return the uptime 
        of your system to the uptime-website.
    """,

    author="Dominick Rivard",
    author_email="dominick.rivard@gmail.com",

    license="GPL3",

    url="",
    
    packages = find_packages("src"), 

    package_dir = {"":"src"},

    zip_safe = True,
    
    install_requires = ["ConfigParser"],
    
    entry_points = {
        "console_scripts": [
            "uptime_client = client.func:main",
        ]
    },
)
