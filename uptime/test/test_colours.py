#!/usr/bin/env python

'''

Python Validators.py Unit tests.

'''

from uptime.colours import *
import unittest

class test_colours(unittest.TestCase):
    
    def setUp(self):
        self.my_test_str = "My sentence is filled with colour."
        
    def test_can_colorize_errors(self):
        # Test if the colorize function can return a RED sentence
        colored_str = RED + self.my_test_str + ENDC
        error_str = errors(self.my_test_str)
        
        self.assertEqual(colored_str, error_str)
        
    def test_can_colorize_warnings(self):
        # Test if the colorize function can return a RED sentence
        colored_str = YELLOW + self.my_test_str + ENDC
        warn_str = warn(self.my_test_str)
        
        self.assertEqual(colored_str, warn_str)
        
    def test_can_colorize_infos(self):
        # Test if the colorize function can return a RED sentence
        colored_str = GREEN + self.my_test_str + ENDC
        infos_str = infos(self.my_test_str)
        
        self.assertEqual(colored_str, infos_str)
        