#!/usr/bin/env python3

import unittest
import os
from calculator.software.calc_software import software_addition , software_subtract , software_multiply , software_division

class TestCalcSoftware(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        os.chdir('..')
        os.system("find . -name '*.pyc' -delete")
        os.system("find . -name '__pycache__' -delete")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_software_addition(self):
        self.assertEqual(software_addition(2,3),5)

    def test_software_subtract(self):
        self.assertEqual(software_subtract(5,3),2)

    def test_software_multiply(self):
        self.assertEqual(software_multiply(2,3),7)

    def test_software_division(self):
        self.assertEqual(software_division(10,5),2)


if __name__ == '__main__':
    unittest.main()
