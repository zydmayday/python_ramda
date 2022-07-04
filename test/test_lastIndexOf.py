
import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/lastIndexOf.js
"""

input = [1, 2, 3, 4, 5, 1]


class TestLastIndexOf(unittest.TestCase):
  def test_returns_a_number_indicating_an_object_last_position_in_a_list(self):
    arr = [0, 10, 20, 30, 0, 10, 20, 30, 0, 10]
    self.assertEqual(7, R.lastIndexOf(30, arr))

  def test_returns_minus_1_if_the_object_is_not_in_the_list(self):
    arr = [0, 10, 20, 30]
    self.assertEqual(-1, R.lastIndexOf(40, arr))

  def test_returns_the_last_index_of_the_first_item(self):
    self.assertEqual(5, R.lastIndexOf(1, input))

  def test_returns_the_index_of_the_last_item(self):
    self.assertEqual(4, R.lastIndexOf(5, input))

  def test_does_not_consider_str_1_equals_to_number_1(self):
    self.assertEqual(-1, R.lastIndexOf('1', ['a', 1, 'a']))

  def test_returns_minus_1_for_an_empty_array(self):
    self.assertEqual(-1, R.lastIndexOf('x', []))

  def test_has_R_equals_semantics(self):
    self.assertEqual(-1, R.lastIndexOf(0.0, [-0.0]))
    self.assertEqual(0, R.lastIndexOf(float('nan'), [float('nan')]))
    self.assertEqual(0, R.lastIndexOf(Just([42]), [Just([42])]))

if __name__ == '__main__':
  unittest.main()
