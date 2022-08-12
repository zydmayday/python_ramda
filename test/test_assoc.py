
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/assoc.js
"""


class TestAssoc(unittest.TestCase):
  def test_makes_a_shallow_clone_of_an_object_overriding_only_the_specific_property(self):
    obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
    obj2 = R.assoc('e', {'x': 42}, obj1)
    self.assertEqual({'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'x': 42}, 'f': 5}, obj2)

    self.assertEqual(obj1['a'], obj2['a'])
    self.assertEqual(obj1['b'], obj2['b'])
    self.assertEqual(obj1['f'], obj2['f'])

  def test_is_the_equivalent_of_clone_and_set_if_the_property_is_not_on_the_original(self):
    obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
    obj2 = R.assoc('z', {'x': 42}, obj1)
    self.assertEqual({'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5, 'z': {'x': 42}}, obj2)

    self.assertEqual(obj1['a'], obj2['a'])
    self.assertEqual(obj1['b'], obj2['b'])
    self.assertEqual(obj1['f'], obj2['f'])

  def test_makes_a_shallow_clone_of_an_array_overriding_only_the_specific_index(self):
    newValue = [4, 2]
    arr1 = [1, [2, 3], 4, 5]
    arr2 = R.assoc(2, newValue, arr1)
    self.assertEqual([1, [2, 3], [4, 2], 5], arr2)

    self.assertEqual(arr1[0], arr2[0])
    self.assertEqual(arr1[1], arr2[1])
    self.assertEqual(newValue, arr2[2])
    self.assertEqual(arr1[3], arr2[3])

  def test_is_the_equivalent_of_clone_and_set_if_the_index_is_not_on_the_original(self):
    newValue = [4, 2]
    arr1 = [1, [2, 3], 4]
    arr2 = R.assoc(5, newValue, arr1)
    self.assertEqual([1, [2, 3], 4, None, None, [4, 2]], arr2)

    self.assertEqual(arr1[0], arr2[0])
    self.assertEqual(arr1[1], arr2[1])
    self.assertEqual(arr1[2], arr2[2])
    self.assertEqual(newValue, arr2[5])


if __name__ == '__main__':
  unittest.main()
