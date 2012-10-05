#!/usr/bin/env python

from uptime.__init__ import __version__ as VERSION
from uptime.__init__ import __website_name__ as WEBSITE_NAME
from uptime.colours import *
from uptime.handler import *
import optparse
import sys

DESCRIPTION = "This program sends the uptime information from this"
DESCRIPTION += " computer to the {website} website."
DESCRIPTION = DESCRIPTION.format(website=WEBSITE_NAME)
USAGE = '''\t%prog [options]'''


def display_options(options):
    '''

    This function displays all the attributes that the uptime client
    gather and pushes to the website, based on the desired options.

    e.g.:
        options::['host','arch','dist','uptime','version',]

    '''

    to_print = '\n\t'

    if "host" in options:
        to_print += colorize("Computer:\t\t", CYAN)
        to_print += hostname_handler() + '\n\t'

    if "uptime" in options:
        days, hours, min, sec, c_uptime, raw_seconds = uptime_handler()
        to_print += colorize("Uptime:\t\t\t", CYAN)
        to_print += c_uptime + '\n\t'

    if "dist" in options:
        to_print += colorize("Distribution:\t\t", CYAN)
        to_print += distribution_handler() + '\n\t'

    if "version" in options:
        to_print += colorize("Distribution version:\t", CYAN)
        to_print += version_handler() + '\n\t'

    if "arch" in options:
        to_print += colorize("Architecture:\t\t", CYAN)
        to_print += architecture_handler() + '\n\t'

    return to_print


def main():
    '''

    Command-line tool to configure and test the daemon
    to update the uptime of your computer to the website.

    '''

    parser = optparse.OptionParser(
        usage=infos(USAGE),
        description=colorize(DESCRIPTION, PURPLE),
        add_help_option=False)

    parser.add_option(
        "-h", "--help",
        action="store_true", dest="help",
        help="Show this help message and exit.")

    parser.add_option(
        "-a", "--all",
        action="store_true", dest="all",
        help='''Return all the information available for this client.
        Does not include the option "-p".'''
    )

    parser.add_option(
        "-r", "--arch",
        action="store_true", dest="architecture",
        help="Return the architecture of the hardware platform."
    )

    parser.add_option(
        "-d", "--distribution",
        action="store_true", dest="distribution",
        help="Return the distribution name."
    )

    parser.add_option(
        "-l", "--dist-version",
        action="store_true", dest="dist_version",
        help="Return the distribution version number."
    )

    parser.add_option(
        "-n", "--hostname",
        action="store_true", dest="hostname",
        help="Return the hostname of the computer."
    )

    parser.add_option(
        "-p", "--push",
        action="store_true", dest="push",
        help="Push the uptime information to the website."
    )

    parser.add_option(
        "-u", "--uptime",
        action="store_true", dest="uptime",
        help="Returns the uptime of the computer."
    )

    parser.add_option(
        "-v", "--version",
        action="store_true", dest="version",
        help="Returns the version of the client."
    )

    '''
    If an option is selected, the options dictionary will be set with
    a key/value pair of the key being the name of the option and the
    the value being True or None.

    e.g.:
        options = {
                    'all': None,
                    'dist_version': None,
                    'hostname': None,
                    'uptime': None,
                    'version': None,
                    'architecture': True,
                    'distribution': None,
                    'push': None,
                }
    '''

    options, args = parser.parse_args()
    options_to_display = ['', ]
    number_of_options = 0
    
    if options.all:
        options_to_display = ['host', 'arch', 'dist', 'uptime', 'version', ]
        number_of_options += 1

    if options.architecture:
        options_to_display.append('arch')
        number_of_options += 1

    if options.distribution:
        options_to_display.append('dist')
        number_of_options += 1

    if options.dist_version:
        options_to_display.append('version')
        number_of_options += 1

    if options.hostname:
        options_to_display.append('host')
        number_of_options += 1

    if options.uptime:
        options_to_display.append('uptime')
        number_of_options += 1

    if options.version:
        print VERSION
        number_of_options += 1

    # Display the requested options
    if options_to_display != ['', ]:
        print display_options(options_to_display)
        number_of_options += 1

    if options.push:
        print 'Will push infos to website'
        number_of_options += 1

    if options.help or number_of_options == 0:
        parser.print_help()
        print '\n'

    return sys.exit(2)


if __name__ == "__main__":
    main()
