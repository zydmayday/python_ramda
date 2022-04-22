import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/flatten.js
"""


class TestFlatten(unittest.TestCase):
  def test_turns_a_nested_list_into_one_flat_list(self):
    nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
    self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], R.flatten(nest))
    nest = [[[[3]], 2, 1], 0, [[-1, -2], -3]]
    self.assertEqual([3, 2, 1, 0, -1, -2, -3], R.flatten(nest))
    self.assertEqual([1, 2, 3, 4, 5], R.flatten([1, 2, 3, 4, 5]))

  def test_is_not_destructive(self):
    nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
    self.assertIsNot(nest, R.flatten(nest))

  # def test_handle_ridiculously_large_inputs(self):
  # TODO: find a good way to test timeout
  #   self.assertEqual(1056003, len(R.flatten([*[1] * 1000000, R.range(0, 56000), 5, 1, 3])))

  def test_handles_array_like_objects(self):
    o = {0: [1, 2, [3]], 1: [], 2: ['a', 'b', 'c', ['d', 'e']]}
    self.assertEqual([1, 2, 3, 'a', 'b', 'c', 'd', 'e'], R.flatten(o))

  def test_flattens_an_array_of_empty_arrays(self):
    self.assertEqual([], R.flatten([[], [], []]))
    self.assertEqual([], R.flatten([]))

if __name__ == '__main__':
  unittest.main()
