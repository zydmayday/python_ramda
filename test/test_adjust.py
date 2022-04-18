import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/adjust.js
"""


class TestAdjust(unittest.TestCase):
  def test_applies_the_given_function_to_the_value_at_the_given_index_of_the_supplied_array(self):
    self.assertEqual([0, 1, 3, 3], R.adjust(2, R.add(1), [0, 1, 2, 3]))

  def test_offsets_negative_indexes_from_the_end_of_the_array(self):
    self.assertEqual([0, 2, 2, 3], R.adjust(-3, R.add(1), [0, 1, 2, 3]))

  def test_returns_the_original_array_if_the_supplied_index_is_out_of_bounds(self):
    arr = [0, 1, 2, 3]
    self.assertEqual(arr, R.adjust(4, R.add(1), arr))
    self.assertEqual(arr, R.adjust(-5, R.add(1), arr))

  def test_does_not_mutate_the_original_array(self):
    arr = [0, 1, 2, 3]
    self.assertEqual([0, 1, 3, 3], R.adjust(2, R.add(1), arr))
    self.assertEqual([0, 1, 2, 3], arr)

  def test_accepts_an_array_like_object(self):
    pass
    # TODO: find a way to implement this in python style


if __name__ == '__main__':
  unittest.main()
