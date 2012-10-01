#!/usr/bin/env python

from uptime.__init__ import __version__ as VERSION

def main():
    """
    
    Command-line tool to configure and test the daemon
    to update the uptime of your computer to the website.
    
    """

    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage=usage)
    
    parser.add_option(
        "-a", "--arch", 
        action="store", type="string", dest="architecture",
        help="Slot number (1-3)"
    )
    
    parser.add_option(
        "-d", "--distribution", 
        action="store", type="string", dest="distribution",
        help="Returns the distribution name."
    )
    
    parser.add_option(
        "-l", "--dist-version", 
        action="store", type="string", dest="dist_version",
        help="Returns the distribution version number."
    )
    
    parser.add_option(
        "-n", "--hostname", 
        action="store", type="string", dest="hostname", 
        help="Returns the hostname of the computer."
    )
    
    parser.add_option(
        "-u", "--uptime", 
        action="store", type="string", dest="uptime", 
        help="Returns the uptime of the computer."
    )
    
    parser.add_option(
        "-v", "--version", 
        action="store", type="string", dest="version",
        help="Returns the version of the client."
    )
    
    options, args = parser.parse_args()
    
    print options
    print args
                
                
        
if __name__ == "__main__":
    main()
