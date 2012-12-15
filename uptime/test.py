#!/usr/bin/env python

'''

Python Unit tests.

'''

from uptime.test.test_validators import test_validators
from uptime.test.test_colours import test_colours
from uptime.test.test_prompt import test_prompt
from uptime.test.test_cli import test_cli
import unittest
import random

class test_random_number(unittest.TestCase):
    
    def setUp(self):
        # This test is a random test and it does not cover any code of 
        # the application, but it makes sure the unittest module works.
        self.seq = range(10)
        
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))      
    
        
if __name__ == '__main__':
    print "Unittest::functionality"
    suite = unittest.TestLoader().loadTestsFromTestCase(test_random_number)
    # run the unit tests
    unittest.TextTestRunner(verbosity=2).run(suite)
    print '\n'
    
    print "Unittest::validators.py"
    suite = unittest.TestLoader().loadTestsFromTestCase(test_validators)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print '\n'
    
    print "Unittest::colours.py"
    suite = unittest.TestLoader().loadTestsFromTestCase(test_colours)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print '\n'
    
    print "Unittest::prompt.py"
    suite = unittest.TestLoader().loadTestsFromTestCase(test_prompt)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print '\n'
    
    print "Unittest::cli.py"
    suite = unittest.TestLoader().loadTestsFromTestCase(test_cli)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print '\n'