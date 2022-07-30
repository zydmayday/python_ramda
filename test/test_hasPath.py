
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/hasPath.js
"""

dictObj = {
    'objVal': {'b': {'c': 'c'}},
    'falseVal': False,
    'nullVal': None,
    'arrayVal': ['arr'],
}


class TestHasPathForDict(unittest.TestCase):
  def test_returns_true_for_existing_path(self):
    self.assertEqual(True, R.hasPath(['objVal'], dictObj))
    self.assertEqual(True, R.hasPath(['objVal', 'b'], dictObj))
    self.assertEqual(True, R.hasPath(['objVal', 'b', 'c'], dictObj))
    self.assertEqual(True, R.hasPath(['arrayVal'], dictObj))

  def test_returns_true_for_existing_path_to_falsy_values(self):
    self.assertEqual(True, R.hasPath(['falseVal'], dictObj))
    self.assertEqual(True, R.hasPath(['nullVal'], dictObj))

  def test_returns_false_for_a_test_for_a_child_to_a_non_object(self):
    self.assertEqual(False, R.hasPath(['nullVal', 'child', 'grandChild'], dictObj))
    self.assertEqual(False, R.hasPath(['falseVal', 'child', 'grandChild'], dictObj))
    self.assertEqual(False, R.hasPath(['arrayVal', 0, 'child', 'grandChild'], dictObj))

  def test_returns_true_for_existing_path_with_indexes(self):
    self.assertEqual(True, R.hasPath(['arrayVal', 0], dictObj))

  def test_returns_false_for_non_existing_path_with_indexes(self):
    self.assertEqual(False, R.hasPath(['arrayVal', 1], dictObj))


class Obj:
  def __init__(self, objVal, falseVal, nullVal, arrayVal):
    self.objVal = objVal
    self.falseVal = falseVal
    self.nullVal = nullVal
    self.arrayVal = arrayVal


class ObjVal:
  def __init__(self, b):
    self.b = b


class B:
  def __init__(self, c):
    self.c = c


obj = Obj(ObjVal(B('c')), False, None, ['arr'])


class TestHasPathForObject(unittest.TestCase):
  def test_returns_true_for_existing_path(self):
    self.assertEqual(True, R.hasPath(['objVal'], obj))
    self.assertEqual(True, R.hasPath(['objVal', 'b'], obj))
    self.assertEqual(True, R.hasPath(['objVal', 'b', 'c'], obj))
    self.assertEqual(True, R.hasPath(['arrayVal'], obj))

  def test_returns_true_for_existing_path_to_falsy_values(self):
    self.assertEqual(True, R.hasPath(['falseVal'], obj))
    self.assertEqual(True, R.hasPath(['nullVal'], obj))

  def test_returns_false_for_a_test_for_a_child_to_a_non_object(self):
    self.assertEqual(False, R.hasPath(['nullVal', 'child', 'grandChild'], obj))
    self.assertEqual(False, R.hasPath(['falseVal', 'child', 'grandChild'], obj))
    self.assertEqual(False, R.hasPath(['arrayVal', 0, 'child', 'grandChild'], obj))

  def test_returns_true_for_existing_path_with_indexes(self):
    self.assertEqual(True, R.hasPath(['arrayVal', 0], obj))

  def test_returns_false_for_non_existing_path_with_indexes(self):
    self.assertEqual(False, R.hasPath(['arrayVal', 1], obj))

  def test_static_variables(self):
    class A:
      static_a = 'static a'
    a = A()
    self.assertEqual(False, R.hasPath(['static_a'], a))

  def test_inherited_variables(self):
    class Parent:
      def __init__(self, a):
        self.a = a

    class Child(Parent):
      def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    c = Child('a', 'b')
    self.assertEqual(True, R.hasPath(['a'], c))
    self.assertEqual(True, R.hasPath(['b'], c))


class TestHasPathForOthers(unittest.TestCase):

  def test_for_paths_in_arrays(self):
    self.assertEqual(True, R.hasPath([0], [1, 2]))
    self.assertEqual(False, R.hasPath([2], [1, 2]))

  def test_returns_false_for_non_object(self):
    self.assertEqual(False, R.hasPath([], dictObj))
    self.assertEqual(False, R.hasPath([], obj))

  def test_paths_on_non_objects(self):
    self.assertEqual(False, R.hasPath(['a', 'b'], None))
    self.assertEqual(False, R.hasPath(['a', 'b'], True))
    self.assertEqual(False, R.hasPath(['a', 'b'], ''))

  def test_currying(self):
    self.assertEqual(True, R.hasPath(['a', 'b'], {'a': {'b': 1}}))


if __name__ == '__main__':
  unittest.main()
