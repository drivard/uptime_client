#!/usr/bin/env python

'''

This file is a library of tool to collect the information
we need to provide to the API of uptime website in order
to update the website with the server/desktop statistics.

'''

import platform
import datetime


def uptime_handler():
    '''

    Read the uptime from /proc/uptime

    First value is the number of seconds the computer is running
    with no downtime, the second value is the number of seconds
    the processor was in idle.

    This function is returning the information about the uptime:

      1. Number of days since no downtime
      2. Number of hours since no downtime
      3. Number of minutes since no downtime
      4. Number of seconds since no downtime
      5. String version of the uptime

    I added the raw uptime data to the return statement, to store
    this information in the DB because I intend to host this project
    on a shared hosting plan and I prefer the client to perform
    the extra cycles of formating the data than my shared server.
    But in any case I need the extra information, I will have it
    to perform extra calculation.

    '''

    raw_seconds = 0

    # Return the uptime minus the milliseconds information
    return days, hours, minutes, seconds, computer_uptime, raw_seconds


def distribution_handler():
    '''

    Read the Distribution name from /etc/issue if it is unable to
    provide it using the platform module.

    This function returns two values:

    1. Name of the distribution
       (e.g.: Debian, CentOs, Scientific Linux)
    2. Version of the distribution (e.g.: 6.0, 6.2, 5.0)

    The first argument is more often the distribution name
    but sometimes it requieres the two first words.

    e.g.: Scientific Linux.

    A pattern I notice is that they use the word release in
    the /etc/issue file between the name of the distribution
    and the version.

    If I use platform.dist() for the distribution name,
    Scientific Linux returns Redhat. What is not totally
    wrong but not so true.

    '''

    return distribution.capitalize()


def version_handler():
    '''

    This function returns the version of the distribution
    using the platform module.

    '''
    return platform.dist()[1]

