#!/usr/bin/env python3

from software.calc_software import addition , subtract , multiply , div
import unittest

class TestCalcSoftware(unittest.TestCase):

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

    def test_addition_calc_software(self):
        self.assertEqual(addition(2,3),5)

    def test_subtract_calc_software(self):
        self.assertEqual(subtract(5,3),2)

    def test_multiply_calc_software(self):
        self.assertEqual(multiply(2,3),6)

    def test_division_calc_software(self):
        self.assertEqual(div(10,5),2)


if __name__ == '__main__':
    unittest.main()
