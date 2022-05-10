
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/product.js
"""


class TestT(unittest.TestCase):
  def test_multiplies_together_the_array_of_numbers_supplied(self):
    self.assertEqual(24, R.product([1, 2, 3, 4]))


if __name__ == '__main__':
  unittest.main()
