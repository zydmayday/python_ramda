import types
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/pipe.js
"""


class TestPipe(unittest.TestCase):
  def test_is_a_variadic_function(self):
    self.assertTrue(type(R.pipe) == types.FunctionType)
    self.assertEqual(0, funcArgsLength(R.pipe))

  def test_performs_left_to_right_function_composition(self):
    def add(a, b, c): return a + b + c
    def inc(a): return a + 1
    def pow(a): return a ** 2
    f = R.pipe(add, inc, pow)
    self.assertEqual(3, funcArgsLength(f))
    self.assertEqual(49, f(1, 2, 3))

  def test_throw_if_given_no_arguments(self):
    with self.assertRaises(Exception):
      R.pipe()

  def test_can_be_applied_to_one_argument(self):
    def f(a, b, c): return [a, b, c]
    g = R.pipe(f)
    self.assertEqual(3, funcArgsLength(g))
    self.assertEqual([1, 2, 3], g(1, 2, 3))


if __name__ == '__main__':
  unittest.main()
