
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/lensIndex.js
"""

testList = [{'a': 1}, {'b': 2}, {'c': 3}]


class TestLensIndex(unittest.TestCase):
  def test_focuses_list_element_at_the_specified_index(self):
    self.assertEqual({'a': 1}, R.view(R.lensIndex(0), testList))

  def test_returns_None_if_the_specified_index_does_not_exist(self):
    self.assertEqual(None, R.view(R.lensIndex(10), testList))

  def test_sets_the_list_value_at_the_specified_index(self):
    self.assertEqual([0, {'b': 2}, {'c': 3}], R.set(R.lensIndex(0), 0, testList))

  def test_applies_function_to_the_value_at_the_specified_list_index(self):
    self.assertEqual([{'a': 1}, {'b': 2}, ['c']], R.over(R.lensIndex(2), R.keys, testList))

  def test_can_be_composed(self):
    nestedList = [0, [10, 11, 12], 1, 2]
    composedLens = R.compose(R.lensIndex(1), R.lensIndex(0))
    self.assertEqual(10, R.view(composedLens, nestedList))

  def test_set_s_get_s_equals_s(self):
    # set s (get s) == s
    self.assertEqual(testList, R.set(R.lensIndex(0), R.view(R.lensIndex(0), testList), testList))

  def test_get_set_s_v_equals_v(self):
    # get (set s v) == v
    self.assertEqual(0, R.view(R.lensIndex(0), R.set(R.lensIndex(0), 0, testList)))

  def test_get_set_set_s_v1_v2_equals_v2(self):
    # get (set (set s v1) v2) == v2
    self.assertEqual(11, R.view(R.lensIndex(0), R.set(R.lensIndex(0), 11, R.set(R.lensIndex(0), 10, testList), testList)))

if __name__ == '__main__':
  unittest.main()
