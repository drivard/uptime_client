#!/usr/bin/env python

'''

The validator function helps in validating the inputs the end user
will write using the command line prompt. They will also be used
by the config parser to ensure the value read from the configuration
file are fine.

'''


import re


def validator(value, regex, compiled=False):
    '''

    This function will help validating the value that we will try to
    write in the configuration file.

    '''
    if not compiled:
        regex = re.compile(regex, re.IGNORECASE)

    return re.search(regex, value) != None


def validate_email(value):
    '''

    This function validate if the input is a valid email address.

    I took the email validation regex from:

    github.com/django/django/blob/master/django/core/validators.py

    '''

    email_regex = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
    r')@((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$)'
    r'|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$',
    re.IGNORECASE)

    return validator(value, email_regex, compiled=True)


def validate_password(value):
    '''

    This function will validate that the password is at least 8
    characters long.

    '''

    return len(value) >= 8
