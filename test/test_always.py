import unittest
from datetime import date

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/always.js
"""


class TestAlways(unittest.TestCase):
  def test_returns_a_function_that_returns_the_object_initially_supplied(self):
    theMeaning = R.always(42)
    self.assertEqual(42, theMeaning())
    self.assertEqual(42, theMeaning(10))
    self.assertEqual(42, theMeaning(False))

  def test_works_with_various_types(self):
    self.assertEqual(False, R.always(False)())
    self.assertEqual('abc', R.always('abc')())
    self.assertEqual({'a': 1, 'b': 2}, R.always({'a': 1, 'b': 2})())
    self.assertEqual({'a': 1, 'b': 2}, R.always({'a': 1, 'b': 2})())
    obj = {'a': 1, 'b': 2}
    self.assertEqual(obj, R.always(obj)())
    self.assertEqual(obj, R.always(obj)())
    now = date(1776, 6, 4)
    self.assertEqual(date(1776, 6, 4), R.always(now)())
    self.assertEqual(None, R.always(None)())


class TestAlwaysProperties(unittest.TestCase):
  def test_returns_initial_argument(self):
    a = 42
    b = 27
    f = R.always(a)
    self.assertTrue(f() == a)
    self.assertTrue(f(b) == a)


if __name__ == '__main__':
  unittest.main()
