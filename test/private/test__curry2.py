import unittest

import ramda as R
from ramda.private._curry2 import _curry2
from ramda.private._helper import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/internal/_curry2.js
"""


def f(a, b): return [a, b]


g = _curry2(f)


class Test_Curry2(unittest.TestCase):
  def test_supports_placeholder(self):
    _ = R.__

    self.assertEqual([1, 2], g(1)(2))
    self.assertEqual([1, 2], g(1, 2))

    self.assertEqual([1, 2], g(_, 2)(1))
    self.assertEqual([1, 2], g(1, _)(2))

    self.assertEqual([1, 2], g(_, _)(1)(2))
    self.assertEqual([1, 2], g(_, _)(1, 2))
    self.assertEqual([1, 2], g(_, _)(_)(1, 2))
    self.assertEqual([1, 2], g(_, _)(_, 2)(1))

  def test_has_2_arity(self):
    self.assertEqual(2, funcArgsLength(g))


if __name__ == '__main__':
  unittest.main()
