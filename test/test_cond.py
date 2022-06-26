
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/cond.js
"""


class TestCond(unittest.TestCase):
  def test_returns_a_function(self):
    self.assertTrue(callable(R.cond([])))

  def test_returns_a_conditional_function(self):
    fn = R.cond([
        [R.equals(0), R.always('water freezes at 0°C')],
        [R.equals(100), R.always('water boils at 0°C')],
        [R.T, lambda temp: f'nothing special happens at {temp}°C']
    ])
    fn = R.cond([
        [R.equals('foo'), R.always(1)],
        [R.equals('bar'), R.always(2)]
    ])
    # self.assertEqual('water freezes at 0°C', fn(0))
    # self.assertEqual('nothing special happens at 50°C', fn(50))
    # self.assertEqual('water boils at 100°C', fn(100))

  def test_returns_a_function_which_returns_None_if_none_of_the_predicates_matches(self):
    fn = R.cond([
        [R.equals('foo'), R.always(1)],
        [R.equals('bar'), R.always(2)]
    ])
    self.assertEqual(None, fn('quux'))

  def test_predicates_are_tested_in_order(self):
    fn = R.cond([
        [R.T, R.always('foo')],
        [R.T, R.always('bar')],
        [R.T, R.always('baz')]
    ])
    self.assertEqual('foo', fn())

  def test_forwards_all_arguments_to_predicates_and_to_transformers(self):
    fn = R.cond([
        [lambda _, x: x == 42, lambda a, b, c: a + b + c]
    ])
    self.assertEqual(46, fn(1, 42, 3))

  def test_cond_with_different_number_of_arguments(self):
    fn = R.cond([
        [lambda a: a == 1, lambda a, *_: f'a == {a}'],
        [lambda a, b: a == b, lambda a, b, *_: f'{a} == {b}'],
        [lambda a, b, c: a == b + c, lambda a, b, c: f'{a} == {b} + {c}'],
    ])
    self.assertEqual('a == 1', fn(1))
    self.assertEqual('a == 1', fn(1, 2))
    self.assertEqual('a == 1', fn(1, 2, 3))
    self.assertEqual('2 == 2', fn(2, 2))
    self.assertEqual('2 == 2', fn(2, 2, 3))
    self.assertEqual('4 == 1 + 3', fn(4, 1, 3))
    self.assertEqual(None, fn(4, 1, 4))

  def test_retains_highest_predicate_arity(self):
    fn = R.cond([
        [R.nAry(2, R.T), R.T],
        [R.nAry(3, R.T), R.T],
        [R.nAry(1, R.T), R.T]
    ])
    self.assertEqual(3, funcArgsLength(fn))


if __name__ == '__main__':
  unittest.main()
