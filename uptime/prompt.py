#!/usr/bin/env python


from uptime.__init__ import __website_name__ as WEBSITE_NAME
from uptime.validators import *
from uptime.colours import *
from getpass import getpass

'''

The prompt library contains all the function that will serve to ask
the end-user his registration information in order to put them in the
configuration file.

'''


def header():
    '''

    This function display the header message.

    '''

    intro = '''
    Welcome to the uptime client configurator.

    We inite you to visite the {website} to register an account.
    If you already have an account please enter the following
    information.
    '''
    intro = intro.format(website=WEBSITE_NAME)

    print infos(intro)


def prompt_password():
    '''

    This function will display the prompt to collect the password of
    the end-user. Then it will validate the password.

    '''

    password = None

    while not password:
        user_input = getpass(prompt="Password: ")

        if validate_password(user_input):
            password = user_input
        else:
            message = "Please enter a valid password."
            print errors(message)

    return password


def prompt_username():
    '''

    This function will display the prompt to collect the username of
    the end-user. Then it will validate the username.

    '''
    username = None

    while not username:
        user_input = raw_input("Username: ")

        if validate_email(user_input):
            username = user_input
        else:
            message = "Please enter a valid username (email address)."
            print errors(message)

    return username


DEFAULT_FOOTER = '''
The configurations have been written to the file:

    {filename}

\033[35mThank you for using: {website}!\033[0m
'''


def footer(filename):
    '''

    This function display the footer message.

    '''

    print DEFAULT_FOOTER.format(website=WEBSITE_NAME, filename=filename)


def prompt_logic():
    '''

    This function print the prompt in order.

    '''

    header()
    username = prompt_username()
    password = prompt_password()

    return username, password
