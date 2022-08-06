
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/assocPath.js
"""


class TestAssocPath(unittest.TestCase):
  def test_makes_a_shallow_clone_of_an_object_overriding_only_what_is_necessary_for_the_path(self):
    obj1 = {'a': {'b': 1, 'c': 2, 'd': {'e': 3}}, 'f': {'g': {'h': 4, 'i': [5, 6, 7], 'j': {'k': 6, 'l': 7}}}, 'm': 8}
    obj2 = R.assocPath(['f', 'g', 'i', 1], 42, obj1)
    self.assertEqual([5, 42, 7], obj2['f']['g']['i'])
    self.assertEqual(obj1['a'], obj2['a'])
    self.assertEqual(obj1['m'], obj2['m'])
    self.assertEqual(obj1['f']['g']['h'], obj2['f']['g']['h'])
    self.assertEqual(obj1['f']['g']['j'], obj2['f']['g']['j'])

  def test_is_the_equivalent_of_clone_and_setPath_if_the_property_is_not_on_the_original(self):
    obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
    obj2 = R.assocPath(['x', 0, 'y'], 42, obj1)
    self.assertEqual({'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5, 'x': [{'y': 42}]}, obj2)
    self.assertEqual(obj1['a'], obj2['a'])
    self.assertEqual(obj1['b'], obj2['b'])
    self.assertEqual(obj1['e'], obj2['e'])
    self.assertEqual(obj1['f'], obj2['f'])

  def test_overwrites_primitive_values_with_keys_in_the_path(self):
    obj1 = {'a': 'str'}
    obj2 = R.assocPath(['a', 'b'], 42, obj1)
    self.assertEqual({'a': {'b': 42}}, obj2)

  def test_empty_path_replaces_the_whole_object(self):
    self.assertEqual(3, R.assocPath([], 3, {'a': 1, 'b': 2}))

  def test_replaces_None_with_a_new_object(self):
    self.assertEqual({'foo': {'bar': {'baz': 42}}}, R.assocPath(['foo', 'bar', 'baz'], 42, {'foo': None}))

  def test_assoc_with_numeric_index(self):
    self.assertEqual(['a'], R.assocPath([0], 'a', []))
    self.assertEqual([['a']], R.assocPath([0, 0], 'a', []))
    self.assertEqual([[None, 'a']], R.assocPath([0, 1], 'a', []))

    self.assertEqual({0: 'a'}, R.assocPath([0], 'a', {}))
    self.assertEqual({0: ['a']}, R.assocPath([0, 0], 'a', {}))

  def test_throws_exception_if_3rd_argument_is_not_array_nor_object(self):
    with self.assertRaises(Exception, msg='We only support dict or array for assoc'):
      R.assocPath([1, 2, 3], 42, 'str')


if __name__ == '__main__':
  unittest.main()
