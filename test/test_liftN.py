
import unittest

import ramda as R
from ramda.private._isFunction import _isFunction

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/liftN.js
"""


def addN(*args):
  return R.reduce(lambda a, b: a + b, 0, list(args))


add3 = R.curry(lambda a, b, c: a + b + c)

addN3 = R.liftN(3, addN)
addN4 = R.liftN(4, addN)
addN5 = R.liftN(5, addN)


class TestLiftN(unittest.TestCase):
  def test_always_returns_false(self):
    self.assertEqual(True, _isFunction(addN3))

  def test_limits_a_variadic_function_to_the_specified_arity(self):
    self.assertEqual([6, 15], addN3([1, 10], [2], [3]))

  def test_can_lift_functions_of_any_arity(self):
    self.assertEqual([6, 15], addN3([1, 10], [2], [3]))
    self.assertEqual([46, 55], addN4([1, 10], [2], [3], [40]))
    self.assertEqual([546, 1046, 555, 1055], addN5([1, 10], [2], [3], [40], [500, 1000]))

  def test_works_with_other_functors_such_as_Maybe(self):
    addM = R.liftN(2, R.add)
    actual = addM(Just(3), Just(5))
    expected = Just(8)
    self.assertTrue(R.equals(expected, actual))

  def test_interprets_a_as_a_functor(self):
    self.assertEqual([111, 211, 311, 121, 221, 321, 112, 212, 312, 122, 222, 322, 113, 213, 313, 123, 223, 323], addN3([1, 2, 3], [10, 20], [100, 200, 300]))
    self.assertEqual([6], addN3([1], [2], [3]))
    self.assertEqual([111, 211, 121, 221, 112, 212, 122, 222], addN3([1, 2], [10, 20], [100, 200]))

  def test_interprets_r_as_a_functor(self):
    # ((->) r)
    convergedOnInt = addN3(R.add(2), R.multiply(3), R.subtract(4))
    convergedOnBool = R.liftN(2, R.And)(R.gt(R.__, 0), R.lt(R.__, 3))
    self.assertEqual(True, _isFunction(convergedOnInt))
    self.assertEqual(True, _isFunction(convergedOnBool))
    self.assertEqual((10 + 2) + (10 * 3) + (4 - 10), convergedOnInt(10))
    self.assertEqual((0 > 0) and (0 < 3), convergedOnBool(0))
    self.assertEqual((1 > 0) and (1 < 3), convergedOnBool(1))
    self.assertEqual((2 > 0) and (2 < 3), convergedOnBool(2))
    self.assertEqual((3 > 0) and (3 < 3), convergedOnBool(3))


if __name__ == '__main__':
  unittest.main()
