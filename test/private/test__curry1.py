import unittest

import ramda as R
from ramda.private._curry1 import _curry1
from ramda.private._inspect import funcArgsLength


def f(a): return [a]


g = _curry1(f)


class Test_Curry1(unittest.TestCase):
  def test_supports_placeholder(self):
    _ = R.__

    self.assertEqual([1], g()(1))
    self.assertEqual([1], g(_)(1))
    self.assertEqual([1], g(1))

  def test_has_1_arity(self):
    self.assertEqual(1, funcArgsLength(g))

  def test_works_even_more_args_provided(self):
    self.assertEqual([1], g(1, 2, 3))


if __name__ == '__main__':
  unittest.main()
