import types
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/compose.js
"""


class TestCompose(unittest.TestCase):
  def test_is_a_variadic_function(self):
    self.assertTrue(type(R.compose) == types.FunctionType)
    self.assertEqual(0, funcArgsLength(R.compose))

  def test_performs_right_to_left_function_composition(self):
    def add(a, b, c): return a + b + c
    def inc(a): return a + 1
    def pow(a): return a ** 2
    f = R.compose(pow, inc, add)
    self.assertEqual(3, funcArgsLength(f))
    self.assertEqual(49, f(1, 2, 3))

  def test_throw_if_given_no_arguments(self):
    with self.assertRaises(Exception):
      R.compose()

  def test_can_be_applied_to_one_argument(self):
    def f(a, b, c): return [a, b, c]
    g = R.compose(f)
    self.assertEqual(3, funcArgsLength(g))
    self.assertEqual([1, 2, 3], g(1, 2, 3))

  def test_composes_two_functions(self):
    def inc(a): return a + 1
    def pow(a): return a ** 2
    self.assertEqual(inc(pow(2)), R.compose(inc, pow)(2))

  def test_associative(self):
    def f(a): return a + 1
    def g(a): return a ** 2
    def h(a): return a * 2
    x = 2
    result = f(g(h(x)))
    self.assertEqual(result, R.compose(f, g, h)(x))
    self.assertEqual(result, R.compose(f, R.compose(g, h))(x))
    self.assertEqual(result, R.compose(R.compose(f, g), h)(x))


if __name__ == '__main__':
  unittest.main()
