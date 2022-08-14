
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/lensProp.js
"""

testDict = {
    'a': 1,
    'b': 2,
    'c': 3
}


class Obj:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c


testObj = Obj(1, 2, 3)


class TestLensProp(unittest.TestCase):
  def test_focuses_object_the_specified_object_property(self):
    self.assertEqual(1, R.view(R.lensProp('a'), testDict))
    self.assertEqual(1, R.view(R.lensProp('a'), testObj))

  def test_returns_None_if_the_specified_property_does_not_exist(self):
    self.assertEqual(None, R.view(R.lensProp('X'), testDict))
    self.assertEqual(None, R.view(R.lensProp('X'), testObj))

  def test_sets_the_value_of_the_object_property_specified(self):
    self.assertEqual({'a': 0, 'b': 2, 'c': 3}, R.set(R.lensProp('a'), 0, testDict))
    # TODO: support object, refer assoc

  def test_adds_the_property_to_the_object_if_it_does_not_exist(self):
    self.assertEqual({'a': 1, 'b': 2, 'c': 3, 'd': 4}, R.set(R.lensProp('d'), 4, testDict))
    # TODO: support object, refer assoc

  def test_applies_function_to_the_value_of_the_specified_object_property(self):
    self.assertEqual({'a': 2, 'b': 2, 'c': 3}, R.over(R.lensProp('a'), R.inc, testDict))
    # TODO: support object, refer assoc

  def test_applies_function_to_the_value_of_the_specified_object_property(self):
    self.assertEqual({'a': 2, 'b': 2, 'c': 3}, R.over(R.lensProp('a'), R.inc, testDict))
    # TODO: support object, refer assoc

  def test_applies_function_to_None_and_adds_the_property_if_it_does_not_exist(self):
    self.assertEqual({'a': 1, 'b': 2, 'c': 3, 'X': None}, R.over(R.lensProp('X'), R.identity, testDict))
    # TODO: support object, refer assoc

  def test_can_be_composed(self):
    nestedObj = {
        'a': {
            'b': 1
        },
        'c': 2
    }
    composedLens = R.compose(R.lensProp('a'), R.lensProp('b'))
    self.assertEqual(1, R.view(composedLens, nestedObj))

  def test_set_s_get_s_equals_s(self):
    # set s (get s) == s
    self.assertEqual(testDict, R.set(R.lensProp('a'), R.view(R.lensProp('a'), testDict), testDict))

  def test_get_set_s_v_equals_s_v(self):
    # get (set s v) == v
    self.assertEqual(1, R.view(R.lensProp('a'), R.set(R.lensProp('a'), 1, testDict)))

  def test_get_set_set_s_v1_v2_equals_v2(self):
    # get (set (set s v1) v2) == v2
    self.assertEqual(11, R.view(R.lensProp('a'), R.set(R.lensProp('a'), 11, R.set(R.lensProp('a'), 10, testDict))))


if __name__ == '__main__':
  unittest.main()
