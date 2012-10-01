#!/usr/bin/env python
#
# This file is a library of tool to collect the information
# we need to provide to the API of uptime website in order 
# to update the website with the server/desktop statistics.
#

import platform
import datetime
import re

def uptime_handler():
    """
    Read the uptime from /proc/uptime
    
    First value is the number of seconds the computer is running
    with no downtime, the second value is the number of seconds
    the processor was in idle.
    """
    with open("/proc/uptime", "r") as file:
        seconds = file.read().split()[0]
        
    # The string containing the uptime information
    computer_uptime = str(datetime.timedelta(seconds=float(seconds)))
    
    # Return the uptime minus the milliseconds information
    return computer_uptime.split('.')[0]
    
def distribution_version_handler():
    """
    Read the Distribution name and version from /etc/issue.
    
    This function returns two values:
    
    1. Name of the distribution (e.g.: Debian, CentOs, Scientific Linux)
    2. Version of the distribution (e.g.: 6.0, 6.2, 5.0)
    """
    with open("/etc/issue", "r") as file:
        release_infos = file.read()
        
    # First argument is more often the distrobution name
    # but sometimes it requieres the two first lines
    # e.g.: Scientific Linux.
    # A pattern a notice is that the use the word release in
    # the /etc/issue file between the name of the distribution
    # and the version
    distribution = release_infos.split('release')[0]
    if distribution == release_infos:
        distribution = release_infos.split()[0]
    distribution.strip()
        
    version = ''
    match = re.search(r'\d\.\d', release_infos)
    version = match.group()
        
    return version, distribution
    
def architecture_handler():
    """
    This function returns the architecture of the hardware
    running the uptime client.
    """
    
    return platform.architecture()[0]