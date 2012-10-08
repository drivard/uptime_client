#!/usr/bin/env python

'''

The validator function helps in validating the inputs the end user
will write using the command line prompt. They will also be used
by the config parser to ensure the value read from the configuration
file are fine.

'''


import re


def validator(value, regex):
    '''

    This function will help validating the value that we will try to
    write in the configuration file.

    '''

    regex = re.compile(regex, re.IGNORECASE)

    return re.match(regex, value) != None


def validate_email(value):
    '''

    This function validate if the input is a valid email address.

    I took the email validation regex from:

    http://www.regular-expressions.info/email.html

    I am still asking myself if I should take the one from Django.

    github.com/django/django/blob/master/django/core/validators.py

    '''

    email_regex = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'

    return validator(value, email_regex)


def validate_password(value):
    '''

    This function will validate that the password is at least 8
    characters long.

    '''

    return len(value) >= 8
