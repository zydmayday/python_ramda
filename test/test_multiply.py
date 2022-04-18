import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/multiply.js
"""


class TestMultiply(unittest.TestCase):
  def test_multiplies_together_two_numbers(self):
    self.assertEqual(42, R.multiply(6, 7))


if __name__ == '__main__':
  unittest.main()
