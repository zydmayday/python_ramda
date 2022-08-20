
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/update.js
"""


class TestUpdate(unittest.TestCase):
  def test_updates_the_value_at_the_given_index_of_the_supplied_array(self):
    self.assertEqual([0, 1, 4, 3], R.update(2, 4, [0, 1, 2, 3]))

  def test_offsets_negative_indexes_from_the_end_of_the_array(self):
    self.assertEqual([0, 4, 2, 3], R.update(-3, 4, [0, 1, 2, 3]))

  def test_returns_the_original_array_if_the_supplied_index_is_out_of_bounds(self):
    arr = [0, 1, 2, 3]
    self.assertEqual(arr, R.update(4, 4, arr))
    self.assertEqual(arr, R.update(-5, 4, arr))

  def test_does_not_mutate_the_original_array(self):
    arr = [0, 1, 2, 3]
    self.assertEqual([0, 1, 4, 3], R.update(2, 4, arr))
    self.assertEqual([0, 1, 2, 3], arr)

  def test_curries_the_arguments(self):
    self.assertEqual([0, 1, 4, 3], R.update(2)(4)([0, 1, 2, 3]))

  def test_accpets_an_array_like_object(self):
    def args(*a):
      return list(a)

    self.assertEqual([0, 1, 4, 3], R.update(2, 4, args(0, 1, 2, 3)))


if __name__ == '__main__':
  unittest.main()
