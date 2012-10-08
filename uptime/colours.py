#!/usr/bin/env python

'''

Let's put some colour to our digital life!

'''

ENDC = '\033[0m'
BLACK = "\033[30m"        # Black
RED = "\033[31m"          # Red
GREEN = "\033[32m"        # Green
YELLOW = "\033[33m"       # Yellow
BLUE = "\033[34m"         # Blue
PURPLE = "\033[35m"       # Purple
CYAN = "\033[36m"         # Cyan
WHITE = "\033[37m"        # White


def colorize(message='', colour=ENDC):
    '''

    Apply the specific colour to the string message.

    '''
    return colour + message + ENDC


def warn(message):
    '''

    Apply and display the warning message using the yellow colour.

    '''

    return colorize(message, YELLOW)


def errors(message):
    '''

    Apply and display the error message using the red colour.

    '''

    return colorize(message, RED)


def infos(message):
    '''

    Apply and display the information message using the green colour.

    '''

    return colorize(message, GREEN)
