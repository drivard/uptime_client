#!/usr/bin/env python

'''

Python Config.py Unit tests.

'''

from uptime.__init__ import __config_file__ as CONFIG_FILE
from uptime.__init__ import __home_folder__ as HOME
from uptime.config import *
import unittest
import mock


class test_config(unittest.TestCase):
    
    def setUp(self):
        self.file_exists = HOME + CONFIG_FILE
        
    def test_file_exists(self):
        open_mock = mock.MagicMock()
        
        with mock.patch('__builtin__.open', open_mock):        
            self.assertEqual(self.file_exists, check_config_file())