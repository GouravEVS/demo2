#!/usr/bin/env python3

import unittest
import os
from calculator.hardware.calc_hardware import hardware_addition , hardware_subtract , hardware_multiply , hardware_division

class TestCalcHardware(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hardware_addition(self):
        self.assertEqual(hardware_addition(2,3),5)

    def test_hardware_subtract(self):
        self.assertEqual(hardware_subtract(5,3),2)

    def test_hardware_multiply(self):
        self.assertEqual(hardware_multiply(2,3),6)

    def test_hardware_division(self):
        self.assertEqual(hardware_division(10,5),2)


if __name__ == '__main__':
    unittest.main()
