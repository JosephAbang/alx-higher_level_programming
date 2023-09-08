#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """Testing edge cases for max integer"""

    def setUp(self):
        self.pos_list = [1, 3, 5, 8, 9, 4]
        self.neg_list = [-1, -3, -5, -8, -9, -4]
        self.err_list = [1, 3, 5, 8, "Hello"]
        self.mix_list = [-1, 4, -4, 5, 6, 7, -2]
        self.float_list = [2, -4, 5.5, 4, 8]

    def test_max_pos_integer(self):
        self.assertEqual(max_integer(self.pos_list), 9)

    def test_max_neg_integer(self):
        self.assertEqual(max_integer(self.neg_list), -1)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_raise_error(self):
        self.assertRaises(TypeError, max_integer, self.err_list)

    def test_mix_integer(self):
        self.assertEqual(max_integer(self.mix_list), 7)

    def test_float_list(self):
        self.assertRaises(TypeError, max_integer, self.float_list)

    def test_single_pos_elem_(self):
        self.assertEqual(max_integer([5]), 5)

    def test_single_pos_elem_(self):
        self.assertEqual(max_integer([-53]), -53)


if __name__ == "__main__":
    unittest.main()
