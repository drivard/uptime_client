#!/usr/bin/env python

'''

Python Prompt.py Unit tests.

'''

from uptime.__init__ import __website_name__ as WEBSITE_NAME
from uptime.__init__ import __config_file__ as CONFIG_FILE
from uptime.__init__ import __home_folder__ as HOME
from uptime.prompt import *
from uptime.colours import *
import unittest

INTRO = '''
Welcome to the uptime client configurator.

We inite you to visite {website} to register an account.
If you already have an account please enter the following
information.

'''

DEFAULT_FOOTER = '''
The configurations have been written to the file:

    {filename}

\033[35mThank you for using: {website}!\033[0m
'''

class test_prompt(unittest.TestCase):
    
    def setUp(self):
        self.header_manual = infos(INTRO.format(website=WEBSITE_NAME))
        self.header_auto = header()
        self.filename = HOME + CONFIG_FILE
        self.footer_manual = DEFAULT_FOOTER.format(
            website=WEBSITE_NAME,
            filename=self.filename)
        self.footer_auto = footer()
        
    def test_can_generate_text_header(self): 
        self.assertEqual(self.header_manual, self.header_auto)
        
    def test_can_generate_text_footer(self): 
        self.assertEqual(self.footer_manual, self.footer_auto)
        
        
    