
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/zipObj.js
"""


class TestZipObj(unittest.TestCase):
  def test_combines_an_array_of_keys_with_an_array_of_values_into_a_single_dict(self):
    self.assertEqual({'a': 1, 'b': 2, 'c': 3}, R.zipObj(['a', 'b', 'c'], [1, 2, 3]))

  def test_ignores_extra_values(self):
    self.assertEqual({'a': 1, 'b': 2, 'c': 3}, R.zipObj(['a', 'b', 'c'], [1, 2, 3, 4, 5, 6, 7]))

  def test_ignores_extra_keys(self):
    self.assertEqual({'a': 1, 'b': 2, 'c': 3}, R.zipObj(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3]))

  def test_last_one_in_wins_when_there_are_duplicate_keys(self):
    self.assertEqual({'a': 'LAST', 'b': 2, 'c': 3}, R.zipObj(['a', 'b', 'c', 'a'], [1, 2, 3, 'LAST']))


if __name__ == '__main__':
  unittest.main()
