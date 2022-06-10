
import unittest
from math import isnan

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/length.js
"""


class TestLength(unittest.TestCase):
  def test_returns_the_length_of_a_list(self):
    self.assertEqual(0, R.length([]))
    self.assertEqual(4, R.length(['a', 'b', 'c', 'd']))

  def test_returns_the_length_of_a_string(self):
    self.assertEqual(0, R.length(''))
    self.assertEqual(3, R.length('xyz'))

  def test_returns_the_length_of_a_function(self):
    self.assertEqual(0, R.length(lambda: None))
    self.assertEqual(3, R.length(lambda x, y, z: z))

  def test_returns_the_length_of_a_dict(self):
    self.assertEqual(0, R.length({}))
    self.assertEqual(2, R.length({'a': 1, 'b': 2}))

  def test_returns_the_length_of_an_arguments_object(self):
    fn = lambda *args: args
    self.assertEqual(0, R.length(fn()))
    self.assertEqual(3, R.length(fn(1, 2, 3)))

  def test_returns_the_length_of_a_set(self):
    self.assertEqual(0, R.length(set()))
    self.assertEqual(3, R.length(set([1, 2, 3])))
    self.assertEqual(3, R.length({1, 2, 3}))

  def test_returns_the_length_of_a_tuple(self):
    self.assertEqual(0, R.length(()))
    self.assertEqual(3, R.length((1, 2, 3)))

  def test_returns_nan_for_value_of_unexpected_type(self):
    self.assertTrue(isnan(R.length(0)))
    self.assertTrue(isnan(R.length(None)))

  def test_returns_nan_for_length_property_of_unexpected_type(self):
    self.assertTrue(isnan(R.length({'length': ''})))
    self.assertTrue(isnan(R.length({'length': '1.23'})))
    self.assertTrue(isnan(R.length({'length': None})))

    class ObjWithoutLength:
      pass
    obj = ObjWithoutLength()
    self.assertTrue(isnan(R.length(obj)))

  def test_use_length_property(self):
    self.assertEqual(100, R.length({'length': 100}))
    self.assertEqual(100, R.length({'a': None, 'length': 100}))

  def test_dispatches_to_object_length(self):
    class Obj:
      def length(self):
        return 100
    obj = Obj()
    self.assertEqual(100, R.length(obj))

  def test_dispatches_to_object_length_return_nan_if_unexpected_type(self):
    class Obj:
      def length(self):
        return '1.23'
    obj = Obj()
    self.assertTrue(isnan(R.length(obj)))


if __name__ == '__main__':
  unittest.main()
