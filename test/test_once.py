
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/once.js
"""


class TestOnce(unittest.TestCase):
  def test_returns_a_function_that_calls_the_supplied_function_only_the_first_time_called(self):
    ctr = 0

    def wrapper():
      nonlocal ctr
      ctr += 1
    fn = R.once(wrapper)
    fn()
    self.assertEqual(1, ctr)
    fn()
    self.assertEqual(1, ctr)
    fn()
    self.assertEqual(1, ctr)

  def test_passes_along_arguments_supplied(self):
    fn = R.once(lambda a, b: a + b)
    result = fn(5, 10)
    self.assertEqual(15, result)

  def test_retains_and_returns_the_first_value_calculated_even_if_different_arguments_are_passed_later(self):
    ctr = 0

    def add(a, b):
      nonlocal ctr
      ctr += 1
      return a + b
    fn = R.once(add)
    result = fn(5, 10)
    self.assertEqual(15, result)
    self.assertEqual(1, ctr)
    result = fn(20, 30)
    self.assertEqual(15, result)
    self.assertEqual(1, ctr)

  def test_retains_arity(self):
    f = R.once(lambda a, b: a + b)
    self.assertEqual(2, funcArgsLength(f))


if __name__ == '__main__':
  unittest.main()
