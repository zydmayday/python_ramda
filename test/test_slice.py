import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/slice.js
"""


class TestSlice(unittest.TestCase):
  def test_retrieves_the_proper_sublist_of_a_list(self):
    list = [8, 6, 7, 5, 3, 0, 9]
    self.assertEqual([7, 5, 3], R.slice(2, 5, list))

  def test_can_operate_on_tuple(self):
    list = (8, 6, 7, 5, 3, 0, 9)
    self.assertEqual((7, 5, 3), R.slice(2, 5, list))

  def test_can_operate_on_strings(self):
    self.assertEqual(R.slice(0, 0, 'abc'), '')
    self.assertEqual(R.slice(0, 1, 'abc'), 'a')
    self.assertEqual(R.slice(0, 2, 'abc'), 'ab')
    self.assertEqual(R.slice(0, 3, 'abc'), 'abc')
    self.assertEqual(R.slice(0, 4, 'abc'), 'abc')
    self.assertEqual(R.slice(1, 0, 'abc'), '')
    self.assertEqual(R.slice(1, 1, 'abc'), '')
    self.assertEqual(R.slice(1, 2, 'abc'), 'b')
    self.assertEqual(R.slice(1, 3, 'abc'), 'bc')
    self.assertEqual(R.slice(1, 4, 'abc'), 'bc')
    self.assertEqual(R.slice(0, -4, 'abc'), '')
    self.assertEqual(R.slice(0, -3, 'abc'), '')
    self.assertEqual(R.slice(0, -2, 'abc'), 'a')
    self.assertEqual(R.slice(0, -1, 'abc'), 'ab')
    self.assertEqual(R.slice(0, -0, 'abc'), '')
    self.assertEqual(R.slice(-2, -4, 'abc'), '')
    self.assertEqual(R.slice(-2, -3, 'abc'), '')
    self.assertEqual(R.slice(-2, -2, 'abc'), '')
    self.assertEqual(R.slice(-2, -1, 'abc'), 'b')
    self.assertEqual(R.slice(-2, -0, 'abc'), '')

class TestSliceDifferentFromRamda(unittest.TestCase):
  def test_support_None_for_second_param(self):
    self.assertEqual(R.slice(0, None, ['a', 'b', 'c']), ['a', 'b', 'c'])
    self.assertEqual(R.slice(1, None, ['a', 'b', 'c']), ['b', 'c'])
    self.assertEqual(R.slice(2, None, ['a', 'b', 'c']), ['c'])
    self.assertEqual(R.slice(3, None, ['a', 'b', 'c']), [])
    self.assertEqual(R.slice(4, None, ['a', 'b', 'c']), [])

    self.assertEqual(R.slice(0, None, 'abc'), 'abc')
    self.assertEqual(R.slice(1, None, 'abc'), 'bc')
    self.assertEqual(R.slice(2, None, 'abc'), 'c')
    self.assertEqual(R.slice(3, None, 'abc'), '')
    self.assertEqual(R.slice(4, None, 'abc'), '')

if __name__ == '__main__':
  unittest.main()
