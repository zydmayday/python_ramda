import unittest
from inspect import getfullargspec
from random import randint

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/curry.js
"""


class TestCurry(unittest.TestCase):
  def test_curries_a_single_value(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = R.curry(e)
    g = f(12)
    self.assertEqual(15, g(3, 6, 2))

  def test_curries_multiple_values(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = R.curry(e)
    g = f(12, 3)
    self.assertEqual(15, g(6, 2))
    h = f(12, 3, 6)
    self.assertEqual(15, h(2))

  def test_allows_further_currying_of_a_curried_function(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = R.curry(e)
    g = f(12)
    self.assertEqual(15, g(3, 6, 2))
    h = g(3)
    self.assertEqual(15, h(6, 2))
    self.assertEqual(15, g(3, 6)(2))

  def test_properly_reports_the_length_of_the_curried_function(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = R.curry(e)
    fullargspec = getfullargspec(f)
    self.assertEqual(4, len(fullargspec.args))

  def test_supports_R_placeholder(self):
    def f(a, b, c):
      return [a, b, c]
    g = R.curry(f)
    _ = R.__

    self.assertEqual([1, 2, 3], g(1)(2)(3))
    self.assertEqual([1, 2, 3], g(1)(2, 3))
    self.assertEqual([1, 2, 3], g(1, 2)(3))
    self.assertEqual([1, 2, 3], g(1, 2, 3))

    self.assertEqual([1, 2, 3], g(_, 2, 3)(1))
    self.assertEqual([1, 2, 3], g(1, _, 3)(2))
    self.assertEqual([1, 2, 3], g(1, 2, _)(3))

    self.assertEqual([1, 2, 3], g(1, _, _)(2)(3))
    self.assertEqual([1, 2, 3], g(_, 2, _)(1)(3))
    self.assertEqual([1, 2, 3], g(_, _, 3)(1)(2))

    self.assertEqual([1, 2, 3], g(1, _, _)(2, 3))
    self.assertEqual([1, 2, 3], g(_, 2, _)(1, 3))
    self.assertEqual([1, 2, 3], g(_, _, 3)(1, 2))

    self.assertEqual([1, 2, 3], g(1, _, _)(_, 3)(2))
    self.assertEqual([1, 2, 3], g(_, 2, _)(_, 3)(1))
    self.assertEqual([1, 2, 3], g(_, _, 3)(_, 2)(1))

    self.assertEqual([1, 2, 3], g(_, _, _)(_, _)(_)(1, 2, 3))
    self.assertEqual([1, 2, 3], g(_, _, _)(1, _, _)(_, _)(2, _)(_)(3))

  def test_supports_functional_placeholder(self):
    def f(a, b, c):
      return [a, b, c]
    g = R.curry(f)
    _ = {'@@functional/placeholder': True, 'x': randint(0, 100)}

    self.assertEqual([1, 2, 3], g(1)(2)(3))
    self.assertEqual([1, 2, 3], g(1)(2, 3))
    self.assertEqual([1, 2, 3], g(1, 2)(3))
    self.assertEqual([1, 2, 3], g(1, 2, 3))

    self.assertEqual([1, 2, 3], g(_, 2, 3)(1))
    self.assertEqual([1, 2, 3], g(1, _, 3)(2))
    self.assertEqual([1, 2, 3], g(1, 2, _)(3))

    self.assertEqual([1, 2, 3], g(1, _, _)(2)(3))
    self.assertEqual([1, 2, 3], g(_, 2, _)(1)(3))
    self.assertEqual([1, 2, 3], g(_, _, 3)(1)(2))

    self.assertEqual([1, 2, 3], g(1, _, _)(2, 3))
    self.assertEqual([1, 2, 3], g(_, 2, _)(1, 3))
    self.assertEqual([1, 2, 3], g(_, _, 3)(1, 2))

    self.assertEqual([1, 2, 3], g(1, _, _)(_, 3)(2))
    self.assertEqual([1, 2, 3], g(_, 2, _)(_, 3)(1))
    self.assertEqual([1, 2, 3], g(_, _, 3)(_, 2)(1))

    self.assertEqual([1, 2, 3], g(_, _, _)(_, _)(_)(1, 2, 3))
    self.assertEqual([1, 2, 3], g(_, _, _)(1, _, _)(_, _)(2, _)(_)(3))

  def test_forwads_extra_arguments(self):
    def f(a, b, c, *args):
      return [a] + [b] + [c] + list(args)
    g = R.curry(f)
    self.assertEqual([1, 2, 3], g(1, 2, 3))
    self.assertEqual([1, 2, 3, 4], g(1, 2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1, 2)(3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2)(3, 4))

  def test_works_even_more_args_provided(self):
    def f(a, b):
      return [a, b]
    g = R.curry(f)
    self.assertEqual([1, 2], g(1, 2, 3))


if __name__ == '__main__':
  unittest.main()
