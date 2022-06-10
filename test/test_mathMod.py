
import unittest
from math import isnan

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/mathMod.js
"""


class TestMathMod(unittest.TestCase):
  def test_requires_integer_arguments(self):
    self.assertTrue(isnan(R.mathMod('s', 3)))
    self.assertTrue(isnan(R.mathMod(3, 's')))
    self.assertTrue(isnan(R.mathMod(12.2, 3)))
    self.assertTrue(isnan(R.mathMod(3, 12.2)))

  def test_computes_the_true_modulo_function(self):
    self.assertEqual(3, R.mathMod(-17, 5))
    self.assertEqual(2, R.mathMod(17, 5))
    self.assertEqual(3, R.mathMod(15, 12))

if __name__ == '__main__':
  unittest.main()
