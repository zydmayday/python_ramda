
import unittest

import ramda as R
from ramda.private._curry2 import _curry2
from ramda.private._isFunction import _isFunction

from .helpers.listXf import listXf

"""
https://github.com/ramda/ramda/blob/master/test/tap.js
"""

appendToList = _curry2(lambda lst, x: lst.append(x))


class TestTap(unittest.TestCase):
  def test_returns_a_function_that_always_returns_its_argument(self):
    f = R.tap(R.identity)
    self.assertTrue(_isFunction(f))
    self.assertEqual(100, f(100))
    self.assertEqual(None, f(None))

  def test_may_take_a_function_as_the_first_argument_that_executes_with_taps_argument(self):
    sideEffect = 0
    self.assertEqual(0, sideEffect)

    def fn(x):
      nonlocal sideEffect
      sideEffect = 'string ' + str(x)
    rv = R.tap(fn, 200)
    self.assertEqual(200, rv)
    self.assertEqual('string 200', sideEffect)

  def test_can_act_as_a_transducer(self):
    sideEffect = []
    numbers = [1, 2, 3, 4, 5]

    xf = R.compose(R.map(R.identity), R.tap(appendToList(sideEffect)))

    self.assertEqual(numbers, R.into([], xf, numbers))
    self.assertEqual(numbers, sideEffect)

  def test_dispatches_to_transformer_objects(self):
    sideEffect = []
    appendToSideEffect = appendToList(sideEffect)

    res = R.tap(appendToSideEffect, listXf)
    self.assertEqual(appendToSideEffect, res.f)
    self.assertEqual(listXf, res.xf)


if __name__ == '__main__':
  unittest.main()
