
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/ifElse.js
"""


def t(a): return a + 1
def v(a): return isinstance(a, int)


identity = R.identity
def isArray(xs): return isinstance(xs, list)


class TestIfElse(unittest.TestCase):
  def test_calls_the_truth_case_function_if_the_validator_returns_a_truthy_value(self):
    self.assertEqual(11, R.ifElse(v, t, identity)(10))

  def test_calls_the_false_case_function_if_the_validator_returns_a_falsy_value(self):
    def v(a): return isinstance(a, int)
    self.assertEqual('hello', R.ifElse(v, t, identity)('hello'))

  def test_calls_the_true_case_on_array_items_and_the_false_case_on_non_array_items(self):
    arr = [[1, 2, 3, 4, 5], 10, [0, 1], 15]
    arrayToLength = R.map(R.ifElse(isArray, R.length, identity))
    self.assertEqual([5, 10, 2, 15], arrayToLength(arr))

  def test_passes_the_arguments_to_the_true_case_function(self):
    def v(*_): return True

    def onTrue(a, b):
      self.assertEqual(a, 123)
      self.assertEqual(b, 'abc')

    R.ifElse(v, onTrue, identity)(123, 'abc')

  def test_passes_the_arguments_to_the_false_case_function(self):
    def v(*_): return False

    def onFalse(a, b):
      self.assertEqual(a, 123)
      self.assertEqual(b, 'abc')

    R.ifElse(v, identity, onFalse)(123, 'abc')

  def test_returns_a_function_whose_arity_equals_the_max_arity_of_the_three_arguments_to_ifElse(self):
    def a0(): return 0
    def a1(x): return x
    def a2(x, y): return x + y

    self.assertEqual(2, funcArgsLength(R.ifElse(a0, a1, a2)))
    self.assertEqual(2, funcArgsLength(R.ifElse(a0, a2, a1)))
    self.assertEqual(2, funcArgsLength(R.ifElse(a1, a0, a2)))
    self.assertEqual(2, funcArgsLength(R.ifElse(a1, a2, a0)))
    self.assertEqual(2, funcArgsLength(R.ifElse(a2, a0, a1)))
    self.assertEqual(2, funcArgsLength(R.ifElse(a2, a1, a0)))

  def test_returns_a_curried_function(self):
    ifIsNumber = R.ifElse(v)
    self.assertEqual(16, ifIsNumber(t, identity)(15))
    self.assertEqual('hello', ifIsNumber(t, identity)('hello'))

    fn = R.ifElse(R.gt, R.subtract, R.add)
    self.assertEqual(9, fn(2)(7))
    self.assertEqual(9, fn(2, 7))
    self.assertEqual(5, fn(7)(2))
    self.assertEqual(5, fn(7, 2))


if __name__ == '__main__':
  unittest.main()
