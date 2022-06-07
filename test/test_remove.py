
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/remove.js
"""

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


class TestRemove(unittest.TestCase):
  def test_splices_out_a_sub_list_of_the_given_list(self):
    self.assertEqual(['a', 'b', 'h', 'i', 'j'], R.remove(2, 5, arr))

  def test_returns_the_appropriate_sublist_with_start_0(self):
    self.assertEqual(['f', 'g', 'h', 'i', 'j'], R.remove(0, 5, arr))
    self.assertEqual(['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], R.remove(0, 1, arr))
    self.assertEqual([], R.remove(0, len(arr), arr))

  def test_removes_the_end_of_the_list_if_the_count_is_too_large(self):
    self.assertEqual(['a', 'b'], R.remove(2, 20, arr))

  def test_retains_the_entire_list_if_the_start_is_too_large(self):
    self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], R.remove(13, 3, arr))


if __name__ == '__main__':
  unittest.main()
