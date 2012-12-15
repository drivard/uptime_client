#!/usr/bin/env python

'''

Python Cli.py Unit tests.

'''

from uptime.colours import *
from uptime.handler import *
from uptime.cli import *
import unittest

options_infos = '\n'
options_infos += colorize("Computer hostname:\t", CYAN)
options_infos += hostname_handler() + '\n'
days, hours, min, sec, c_uptime, raw_seconds = uptime_handler()
options_infos += colorize("Uptime:\t\t\t", CYAN)
options_infos += c_uptime + '\n'
options_infos += colorize("Distribution:\t\t", CYAN)
options_infos += distribution_handler() + '\n'
options_infos += colorize("Distribution version:\t", CYAN)
options_infos += version_handler() + '\n'
options_infos += colorize("Architecture:\t\t", CYAN)
options_infos += architecture_handler() + '\n'


class test_cli(unittest.TestCase):
    
    def setUp(self):
        self.infos = options_infos
        
    def test_displays_options(self):
        s_infos = display_options(['host','arch','dist','uptime','version',])
        
        self.assertEqual(self.infos, s_infos)