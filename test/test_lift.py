
import unittest

import ramda as R
from ramda.private._isFunction import _isFunction

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/lift.js
"""

add3 = R.curry(lambda a, b, c: a + b + c)
add4 = R.curry(lambda a, b, c, d: a + b + c + d)
add5 = R.curry(lambda a, b, c, d, e: a + b + c + d + e)
complement = R.lift(R.Not)
madd3 = R.lift(add3)
madd4 = R.lift(add4)
madd5 = R.lift(add5)


class TestLift(unittest.TestCase):
  def test_returns_a_function_if_called_with_just_a_function(self):
    self.assertEqual(True, _isFunction(R.lift(R.add)))

  def test_produces_a_cross_product_of_array_values(self):
    self.assertEqual([3, 4, 5, 4, 5, 6, 4, 5, 6, 5, 6, 7, 5, 6, 7, 6, 7, 8], madd3([1, 2, 3], [1, 2], [1, 2, 3]))
    self.assertEqual([6], madd3([1], [2], [3]))
    self.assertEqual([9, 10, 10, 11, 10, 11, 11, 12], madd3([1, 2], [3, 4], [5, 6]))

  def test_can_lift_functions_of_any_arity(self):
    self.assertEqual(False, complement(R.isNil)(None))
    self.assertEqual([6, 15], madd3([1, 10], [2], [3]))
    self.assertEqual([46, 55], madd4([1, 10], [2], [3], [40]))
    self.assertEqual([546, 1046, 555, 1055], madd5([1, 10], [2], [3], [40], [500, 1000]))

  def test_works_with_other_functors_such_as_maybe(self):
    addM = R.lift(R.add)
    self.assertEqual(True, R.equals(Just(8), addM(Just(3), Just(5))))

if __name__ == '__main__':
  unittest.main()
