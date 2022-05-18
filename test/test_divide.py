import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/divide.js
"""


class TestDivide(unittest.TestCase):
  def test_divides_two_numbers(self):
    self.assertEqual(4, R.divide(28, 7))


if __name__ == '__main__':
  unittest.main()
