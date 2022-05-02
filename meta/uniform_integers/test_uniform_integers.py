import unittest

from meta.uniform_integers.uniform_integers import getUniformIntegerCountInInterval, getNextUniform


class TestUniformIntegers(unittest.TestCase):

    def test_uniform_integers(self):
        # Sample test case #1
        self.assertEqual(5, getUniformIntegerCountInInterval(75, 300))
        # In the first case, the uniform integers between 7575 and 300300 are 7777, 8888, 9999, 111111, and 222222.

        # Sample test case #2
        self.assertEqual(9, getUniformIntegerCountInInterval(1, 9))
        # In the second case, all 99 single-digit integers between 11 and 99 (inclusive) are uniform.

        # Sample test case #3
        self.assertEqual(1, getUniformIntegerCountInInterval(999999999999, 999999999999))
        # In the third case, the single integer under consideration (999,999,999,999) is uniform.

    def test_next_uniform(self):
        self.assertEqual(2, getNextUniform(1))
        self.assertEqual(11, getNextUniform(10))
        self.assertEqual(22, getNextUniform(11))
        self.assertEqual(2222, getNextUniform(2122))
        self.assertEqual(3333, getNextUniform(2222))
        self.assertEqual(3333, getNextUniform(2223))
        self.assertEqual(3333, getNextUniform(2912))
        self.assertEqual(888, getNextUniform(880))
        self.assertEqual(999, getNextUniform(888))
        self.assertEqual(999, getNextUniform(889))
        self.assertEqual(11111, getNextUniform(9999))
