
import unittest
from datetime import date
from math import isnan

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/subtract.js
"""


class TestSubtract(unittest.TestCase):
  def test_subtracts_two_numbers(self):
    self.assertEqual(15, R.subtract(22, 7))

  def test_coerces_its_arguments_to_numbers(self):
    self.assertEqual(-1, R.subtract('1', '2'))
    self.assertEqual(-1, R.subtract(1, '2'))
    self.assertEqual(1, R.subtract(True, False))
    self.assertTrue(isnan(R.subtract(None, None)))
    self.assertTrue(isnan(R.subtract(date(1, 1, 1), date(2, 1, 1))))


if __name__ == '__main__':
  unittest.main()
