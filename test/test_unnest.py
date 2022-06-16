
import unittest

import ramda as R

from .helpers.Maybe import Just, Nothing

"""
https://github.com/ramda/ramda/blob/master/test/unnest.js
"""


class TestUnnest(unittest.TestCase):
  def test_only_flattens_one_layer_deep_of_a_nested_list(self):
    nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
    self.assertEqual([1, 2, 3, [4, 5], 6, [[[7], 8]], 9, 10], R.unnest(nest))
    nest = [[[[3]], 2, 1], 0, [[-1, -2], -3]]
    self.assertEqual([[[3]], 2, 1, 0, [-1, -2], -3], R.unnest(nest))
    self.assertEqual([1, 2, 3, 4, 5], R.unnest([1, 2, 3, 4, 5]))

  def test_is_not_destructive(self):
    nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
    self.assertNotEqual(nest, R.unnest(nest))

  def test_flattens_an_array_of_empty_arrays(self):
    self.assertEqual([], R.unnest([[], [], []]))
    self.assertEqual([], R.unnest([]))

  def test_is_equivalent_to_R_chain_R_identity(self):
    self.assertTrue(R.unnest(Nothing()).isNothing)
    self.assertTrue(R.unnest(Just(Nothing())).isNothing)
    self.assertTrue(R.equals(Just(Nothing()), R.unnest(Just(Just(Nothing())))))
    self.assertTrue(R.equals(Just(42), R.unnest(Just(Just(42)))))
    self.assertTrue(R.equals(Just(Just(42)), R.unnest(Just(Just(Just(42))))))


if __name__ == '__main__':
  unittest.main()
