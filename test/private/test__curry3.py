
import unittest

import ramda as R
from ramda.private._curry3 import _curry3
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/internal/_curry3.js
"""


def f(a, b, c): return [a, b, c]


g = _curry3(f)


class Test_Curry3(unittest.TestCase):
  def test_supports_placeholder(self):
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

    self.assertEqual([1, 2, 3], g(_, _, _)(_, _)(1, 2, 3))
    self.assertEqual([1, 2, 3], g(_, _, _)(1, _, _)(_, _)(2, _)(_)(3))

  def test_has_3_arity(self):
    self.assertEqual(3, funcArgsLength(g))

  def test_works_even_more_args_provided(self):
    self.assertEqual([1, 2, 3], g(1, 2, 3, 4))


if __name__ == '__main__':
  unittest.main()
