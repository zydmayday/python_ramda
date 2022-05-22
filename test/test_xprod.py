
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/xprod.js
"""


class TestXProd(unittest.TestCase):
  def test_returns_an_empty_list_if_either_input_list_is_empty(self):
    self.assertEqual([], R.xprod([], [1, 2, 3]))
    self.assertEqual([], R.xprod([1, 2, 3], []))

  def test_creates_the_collection_of_all_cross_product_pairs_of_its_parameters(self):
    self.assertEqual([[1, 'a'], [1, 'b'], [1, 'c'], [2, 'a'], [2, 'b'], [2, 'c']], R.xprod([1, 2], ['a', 'b', 'c']))


if __name__ == '__main__':
  unittest.main()
