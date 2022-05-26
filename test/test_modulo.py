
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/modulo.js
"""


class TestModulo(unittest.TestCase):
  def test_divedes_the_first_param_by_the_second_and_returns_the_remainder(self):
    self.assertEqual(0, R.modulo(100, 2))
    self.assertEqual(1, R.modulo(100, 3))
    self.assertEqual(15, R.modulo(100, 17))

  def test_preserves_python_style_modulo_evaluation_for_negative_numbers(self):
    self.assertEqual(3, R.modulo(-5, 4))


if __name__ == '__main__':
  unittest.main()
