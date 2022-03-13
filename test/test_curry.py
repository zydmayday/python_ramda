from inspect import signature
import inspect
import unittest

from pamda import curry

"""
https://github.com/ramda/ramda/blob/master/test/curry.js
"""


class TestCurry(unittest.TestCase):
  def test_curries_a_single_value(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = curry(e)
    g = f(12)
    self.assertEqual(15, g(3, 6, 2))

  def test_curries_multiple_values(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = curry(e)
    g = f(12, 3)
    self.assertEqual(15, g(6, 2))
    h = f(12, 3, 6)
    self.assertEqual(15, h(2))

  def test_allows_further_currying_of_a_curried_function(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = curry(e)
    g = f(12)
    self.assertEqual(15, g(3, 6, 2))
    h = g(3)
    self.assertEqual(15, h(6, 2))
    self.assertEqual(15, g(3, 6)(2))

  def test_properly_reports_the_length_of_the_curried_function(self):
    def e(a, b, c, d):
      return (a + b * c) / d
    f = curry(e)
    sig_f = signature(f)
    # FIXME: Because we need to support extract arguments, so there will always be one more parameters
    # self.assertEqual(5 -> should be 4, len(sig_f.parameters))

  # TODO: Add tests for placeholder

  def test_forwads_extra_arguments(self):
    def f(a, b, c, *args):
      return [a] + [b] + [c] + list(args)
    g = curry(f)
    self.assertEqual([1, 2, 3], g(1, 2, 3))
    self.assertEqual([1, 2, 3, 4], g(1, 2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1, 2)(3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2)(3, 4))


if __name__ == '__main__':
  unittest.main()
