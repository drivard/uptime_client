#!/usr/bin/env python

from uptime.__init__ import __version__ as VERSION
from uptime.__init__ import __website_name__ as WEBSITE_NAME
from uptime.colours import *
from uptime.handler import *
import optparse
import sys

DESCRIPTION = '''This program sends the uptime information from this
computer to the {website} website.'''.format(website=WEBSITE_NAME)
USAGE = '''\t%prog [options]'''

def main():
    '''
    
    Command-line tool to configure and test the daemon
    to update the uptime of your computer to the website.
    
    '''
    
    parser = optparse.OptionParser(
        usage=infos(USAGE),
        description=colorize(DESCRIPTION, PURPLE)
    )
    
    parser.add_option(
        "-a", "--all", 
        action="store_true", dest="all",
        help="Returns all the information available for this client."
    )
    
    parser.add_option(
        "-r", "--arch", 
        action="store_true", dest="architecture",
        help="Returns the architecture of the hardware platform."
    )
    
    parser.add_option(
        "-d", "--distribution", 
        action="store_true", dest="distribution",
        help="Returns the distribution name."
    )
    
    parser.add_option(
        "-l", "--dist-version", 
        action="store_true", dest="dist_version",
        help="Returns the distribution version number."
    )
    
    parser.add_option(
        "-n", "--hostname", 
        action="store_true", dest="hostname", 
        help="Returns the hostname of the computer."
    )
    
    parser.add_option(
        "-p", "--push", 
        action="store_true", dest="push",
        help="Pushes the uptime information to the website."
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
    the value being True.
    
    e.g.: 
        options = {
                    'all': None,
                    'dist_version': None,
                    'hostname': None,
                    'uptime': None,
                    'version': None,
                    'architecture': True,
                    'distribution': None
                }
    '''
    
    options, args = parser.parse_args()
    
    if options.all:
        print 'all'
    elif options.architecture:
        print architecture_handler()
    elif options.distribution:
        print distribution_handler()
    elif options.dist_version:
        print version_handler()
    elif options.hostname:
        print hostname_handler()
    elif options.uptime:
        print uptime_handler()
    elif options.push:
        print 'Will push to website'
    elif options.version:
        print VERSION
    else:
        parser.print_help()
        
    print options.get('architecture')
        
    return sys.exit(2)
                
                
        
if __name__ == "__main__":
    main()
