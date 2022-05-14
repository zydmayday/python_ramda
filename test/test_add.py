import unittest
from datetime import date
from math import isnan

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/add.js
"""


class TestAdd(unittest.TestCase):
  def test_adds_together_two_numbers(self):
    self.assertEqual(10, R.add(3, 7))

  def test_coerces_its_arguments_to_numbers(self):
    self.assertEqual(3, R.add('1', '2'))
    self.assertEqual(3, R.add(1, '2'))
    self.assertEqual(1, R.add(True, False))
    self.assertTrue(isnan(R.add(None, None)))
    self.assertTrue(isnan(R.add(date(1, 1, 1), date(2, 1, 1))))

  def test_float(self):
    self.assertEqual(4.2, R.add(1.1, 3.1))
    self.assertEqual(4.2, R.add('1.1', 3.1))
    self.assertEqual(4.2, R.add('1.1', '3.1'))


class TestAddProperties(unittest.TestCase):
  def test_commutative(self):
    self.assertEqual(R.add(1, 2), R.add(2, 1))

  def test_associative(self):
    self.assertEqual(R.add(1, R.add(2, 3)), R.add(R.add(1, 2), 3))

  def test_identity(self):
    self.assertEqual(R.add(1, 0), 1)
    self.assertEqual(1, R.add(0, 1))


if __name__ == '__main__':
  unittest.main()
