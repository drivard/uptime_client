#!/usr/bin/env python

'''

Python Validators.py Unit tests.

'''

from uptime.validators import *
import unittest

class test_validators(unittest.TestCase):
    
    def setUp(self):
        self.password = "test1234"
        self.bad_password = "123456"
        self.email = "dominick.rivard@gmail.com"
        self.bad_email = "dominick.rivard@"
        self.uncompiled_regex = "(World)"
        self.str_to_match = "HelloWorld"
        
    def test_good_email_validator(self):
        self.assertTrue(validate_email(self.email))
        
    def test_bad_email_validator(self):
        self.assertFalse(validate_email(self.bad_email))
        
    def test_good_password_validator(self):
        self.assertTrue(validate_password(self.password))
        
    def test_bad_password_validator(self):
        self.assertFalse(validate_password(self.bad_password))
        
    def test_not_compiled_regex(self):        
        self.assertTrue(validator(self.str_to_match, self.uncompiled_regex))
        
