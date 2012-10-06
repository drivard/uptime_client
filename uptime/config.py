#!/usr/bin/env python

'''

The config library reads the ~/.uptime/uptime.conf file to read
the user account information that will be used to publish the
information to the website.

'''

from uptime.__init__ import __config_folder__ as CONFIG_FOLDER
from uptime.__init__ import __config_file__ as CONFIG_FILE
from ConfigParser import ConfigParser
import os
import re


def check_config_file():
    '''

    This function will verify the existance of the configuration file.
    If the file doesn't exist it will create it.

    '''

    HOME = os.path.expanduser('~')

    # Create the folder if it doesn't exists
    if not os.path.isdir(HOME + CONFIG_FOLDER):
        os.mkdir(HOME + CONFIG_FOLDER)

    # Create the configuration file if it doesn't exists
    config_file = HOME + CONFIG_FILE

    if not os.path.isfile(config_file):
        with open(config_file, 'w') as file:
            file.close()

    return config_file


def load_config_file(filename):
    '''

    This function load all the configuration from the file located in
    ~/.uptime/uptime.conf and return all the information.

    '''

    config = ConfigParser()
    config.read(filename)

    sections = config.sections()

    options = []

    for s in sections:
        options.extend(config.items(s))

    configs = {}

    for opt in options:
        configs[opt[0]] = opt[1]

    return configs


def write_config(filename, section, option, value):
    '''

    This function will write the configuration to the file.

    '''

    config = ConfigParser()
    config.read(filename)

    if not config.has_section(section):
        config.add_section(section)

    with open(filename, "w") as file:
        config.set(section, option, value)
        config.write(file)

    return section, option, value


def validate_option_value(value, exp):
    '''

    This function will help validating the value that we will try to
    write in the configuration file.

    the regex is from http://www.regular-expressions.info/email.html
    @regex: "\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b"

    '''

    searched = re.search(exp, value)

    return True
