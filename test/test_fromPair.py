
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/fromPair.js
"""


class TestFromPair(unittest.TestCase):
  def test_combines_an_array_of_two_element_arrays_into_a_dict(self):
    self.assertEqual({'a': 1, 'b': 2, 'c': 3}, R.fromPairs([['a', 1], ['b', 2], ['c', 3]]))

  def test_gives_later_entries_precedence_over_earlier_ones(self):
    self.assertEqual({'x': 2}, R.fromPairs([['x', 1], ['x', 2]]))

if __name__ == '__main__':
  unittest.main()
