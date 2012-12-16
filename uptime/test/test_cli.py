#!/usr/bin/env python

'''

Python Cli.py Unit tests.

'''

from StringIO import StringIO
from uptime.colours import *
from uptime.handler import *
from uptime.cli import *
import unittest
import mock

options_infos = '\n'
options_infos += colorize("Computer hostname:\t", CYAN)
options_infos += hostname_handler() + '\n'
days, hours, min, sec, c_uptime, raw_seconds = uptime_handler()
options_infos += colorize("Uptime:\t\t\t", CYAN)
options_infos += str(days) + ' '
options_infos += 'days, ' if days > 1 else 'day, '
options_infos += hours + ':' + min + ':' + sec + '\n'
options_infos += colorize("Distribution:\t\t", CYAN)
options_infos += distribution_handler() + '\n'
options_infos += colorize("Distribution version:\t", CYAN)
options_infos += version_handler() + '\n'
options_infos += colorize("Architecture:\t\t", CYAN)
options_infos += architecture_handler() + '\n'


class test_cli(unittest.TestCase):
    
    def setUp(self):
        self.infos = options_infos
        self.dist = "Redhat"
        
    def test_displays_options(self):
        s_infos = display_options(['host','arch','dist','uptime','version',])
        
        self.assertEqual(self.infos, s_infos)
        
    def test_handler_distribution(self):
        open_mock = mock.MagicMock()
        # open_mock.return_value = 'Redhat'
        
        with mock.patch('__builtin__.open', open_mock):     
            distribution = distribution_handler(dist="redhat")
            
            self.assertTrue(bool(distribution))
        