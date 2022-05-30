
import unittest
from random import randint

import ramda as R
from ramda.private._inspect import funcArgsLength


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

  def test_return_proper_arity_with_given_arity_number(self):
    def f0():
      return 0
    self.assertEqual(0, funcArgsLength(R.curryN(0, f0)))
    def f1(x1): return [x1]
    self.assertEqual(1, funcArgsLength(R.curryN(1, f1)))
    def f2(x1, x2): return [x1, x2]
    self.assertEqual(2, funcArgsLength(R.curryN(2, f2)))
    def f3(x1, x2, x3): return [x1, x2, x3]
    self.assertEqual(3, funcArgsLength(R.curryN(3, f3)))
    def f4(x1, x2, x3, x4): return [x1, x2, x3, x4]
    self.assertEqual(4, funcArgsLength(R.curryN(4, f4)))
    def f5(x1, x2, x3, x4, x5): return [x1, x2, x3, x4, x5]
    self.assertEqual(5, funcArgsLength(R.curryN(5, f5)))
    def f6(x1, x2, x3, x4, x5, x6): return [x1, x2, x3, x4, x5, x6]
    self.assertEqual(6, funcArgsLength(R.curryN(6, f6)))
    def f7(x1, x2, x3, x4, x5, x6, x7): return [x1, x2, x3, x4, x5, x6, x7]
    self.assertEqual(7, funcArgsLength(R.curryN(7, f7)))
    def f8(x1, x2, x3, x4, x5, x6, x7, x8): return [x1, x2, x3, x4, x5, x6, x7, x8]
    self.assertEqual(8, funcArgsLength(R.curryN(8, f8)))
    def f9(x1, x2, x3, x4, x5, x6, x7, x8, x9): return [x1, x2, x3, x4, x5, x6, x7, x8, x9]
    self.assertEqual(9, funcArgsLength(R.curryN(9, f9)))
    def f10(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10): return [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    self.assertEqual(10, funcArgsLength(R.curryN(10, f10)))
    with self.assertRaises(Exception):
      def f11(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11): return [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
      R.curryN(11, f11)

  def test_returned_function_can_be_called_with_proper_arity(self):
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    def f11(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11): return [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

    self.assertEqual(0, funcArgsLength(R.curryN(0, f11)))
    self.assertEqual(expected, R.curryN(0, f11)(*expected))  # need to provide all args at once
    self.assertEqual(1, funcArgsLength(R.curryN(1, f11)))
    self.assertEqual(expected, R.curryN(1, f11)(*expected))  # need to provide all args at once
    self.assertEqual(2, funcArgsLength(R.curryN(2, f11)))
    self.assertEqual(expected, R.curryN(2, f11)(1)(*expected[1:]))
    self.assertEqual(3, funcArgsLength(R.curryN(3, f11)))
    self.assertEqual(expected, R.curryN(3, f11)(1)(2)(*expected[2:]))
    self.assertEqual(4, funcArgsLength(R.curryN(4, f11)))
    self.assertEqual(expected, R.curryN(4, f11)(1)(2)(3)(*expected[3:]))
    self.assertEqual(5, funcArgsLength(R.curryN(5, f11)))
    self.assertEqual(expected, R.curryN(5, f11)(1)(2)(3)(4)(*expected[4:]))
    self.assertEqual(6, funcArgsLength(R.curryN(6, f11)))
    self.assertEqual(expected, R.curryN(6, f11)(1)(2)(3)(4)(5)(*expected[5:]))
    self.assertEqual(7, funcArgsLength(R.curryN(7, f11)))
    self.assertEqual(expected, R.curryN(7, f11)(1)(2)(3)(4)(5)(6)(*expected[6:]))
    self.assertEqual(8, funcArgsLength(R.curryN(8, f11)))
    self.assertEqual(expected, R.curryN(8, f11)(1)(2)(3)(4)(5)(6)(7)(*expected[7:]))
    self.assertEqual(9, funcArgsLength(R.curryN(9, f11)))
    self.assertEqual(expected, R.curryN(9, f11)(1)(2)(3)(4)(5)(6)(7)(8)(*expected[8:]))
    self.assertEqual(10, funcArgsLength(R.curryN(10, f11)))
    self.assertEqual(expected, R.curryN(10, f11)(1)(2)(3)(4)(5)(6)(7)(8)(9)(*expected[9:]))

  def test_works_even_more_args_provided(self):
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    def f11(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11): return [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

    self.assertEqual(expected, R.curryN(0, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(1, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(2, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(3, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(4, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(5, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(6, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(7, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(8, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(9, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    self.assertEqual(expected, R.curryN(10, f11)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))


if __name__ == '__main__':
  unittest.main()
