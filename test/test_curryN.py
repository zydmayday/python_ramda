
import unittest
from random import randint

import pamda as R


def source(a, b, c):
  return a * b * c


'''
https://github.com/ramda/ramda/blob/master/test/curryN.js
'''


class TestCurryN(unittest.TestCase):

  def test_accepts_an_arity(self):
    curried = R.curryN(3, source)
    self.assertEqual(6, curried(1)(2)(3))
    self.assertEqual(6, curried(1, 2)(3))
    self.assertEqual(6, curried(1)(2, 3))
    self.assertEqual(6, curried(1, 2, 3))

  def test_can_be_partially_applied(self):
    curry3 = R.curryN(3)
    curried = curry3(source)
    self.assertEqual(6, curried(1)(2)(3))
    self.assertEqual(6, curried(1, 2)(3))
    self.assertEqual(6, curried(1)(2, 3))
    self.assertEqual(6, curried(1, 2, 3))

  def test_supports_R_placeholder(self):
    def f(*arguments):
      return list(arguments)
    g = R.curryN(3, f)
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
    def f(*arguments):
      return list(arguments)
    g = R.curryN(3, f)
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

  def test_forwards_extra_arguments(self):
    def f(*arguments):
      return list(arguments)
    g = R.curryN(3, f)
    self.assertEqual([1, 2, 3], g(1, 2, 3))
    self.assertEqual([1, 2, 3, 4], g(1, 2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1, 2)(3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2)(3, 4))


if __name__ == '__main__':
  unittest.main()
