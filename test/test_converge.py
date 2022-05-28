
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/converge.js
"""

f1 = R.converge(R.multiply, [R.identity, R.identity])
f2 = R.converge(R.multiply, [R.identity, lambda a, b: b])
f3 = R.converge(R.multiply, [R.identity, lambda a, b, c: c])


class TestConverge(unittest.TestCase):
  def test_passes_the_results_of_applying_the_arguments_individually_to_two_separate_functions_into_a_single_one(self):
    self.assertEqual(15, R.converge(R.multiply, [R.add(1), R.add(3)])(2))

  def test_returns_a_function_with_the_length_of_the_longest_argument(self):
    self.assertEqual(1, funcArgsLength(f1))
    self.assertEqual(2, funcArgsLength(f2))
    self.assertEqual(3, funcArgsLength(f3))

  def test_returns_a_curried_function(self):
    self.assertEqual(42, f2(6)(7))
    self.assertEqual(3, funcArgsLength(f3(R.__)))

  def test_works_with_empty_functions_list(self):
    fn = R.converge(lambda *args: len(args), [])
    self.assertEqual(0, funcArgsLength(fn))
    self.assertEqual(0, fn())

  def test_works_with_functions_with_different_number_of_arguments(self):
    fn = R.converge(R.multiply, [R.add, R.add(1)])
    self.assertEqual(6, fn(1)(2))  # curried
    self.assertEqual(6, fn(1, 2))
    self.assertEqual(6, fn(1)(R.__)(2))
    self.assertEqual(9, fn(R.__, 1)(2))
    self.assertEqual(6, fn(R.__, R.__)(1, 2))
    self.assertEqual(6, fn(1, R.__)(2))
    self.assertEqual(6, fn(1, 2, 3))  # works even more arguments provided


if __name__ == '__main__':
  unittest.main()
