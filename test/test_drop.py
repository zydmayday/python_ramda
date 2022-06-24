import unittest

import ramda as R

from .helpers.listXf import listXfPushData

"""
https://github.com/ramda/ramda/blob/master/test/drop.js
"""


class TestDrop(unittest.TestCase):
  def test_skips_the_first_n_elements_from_a_list_returning_the_remainder(self):
    self.assertEqual(['d', 'e', 'f', 'g'], R.drop(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))

  def test_returns_an_empty_array_if_n_is_too_large(self):
    self.assertEqual([], R.drop(20, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))

  def test_returns_an_equivalent_list_if_n_is_less_than_0(self):
    self.assertEqual([1, 2, 3], R.drop(0, [1, 2, 3]))
    self.assertEqual([1, 2, 3], R.drop(-1, [1, 2, 3]))

  def test_never_returns_the_input_array(self):
    xs = [1, 2, 3]
    self.assertEqual(False, xs is R.drop(0, xs))
    self.assertEqual(False, xs is R.drop(-1, xs))

  def test_can_operate_on_strings(self):
    self.assertEqual('da', R.drop(3, 'Ramda'))
    self.assertEqual('a', R.drop(4, 'Ramda'))
    self.assertEqual('', R.drop(5, 'Ramda'))
    self.assertEqual('', R.drop(6, 'Ramda'))

  def test_drop_xf(self):
    dropXf = R.drop(2, listXfPushData)
    res = R.reduce(dropXf, [], [1, 2, 3, 4, 5])
    self.assertEqual([3, 4, 5], res)


if __name__ == '__main__':
  unittest.main()
