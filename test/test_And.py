
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/and.js
"""


class TestAnd(unittest.TestCase):
  def test_compares_two_values_with_python_and(self):
    self.assertEqual(True, R.And(True, True))
    self.assertEqual(False, R.And(True, False))
    self.assertEqual(False, R.And(False, True))
    self.assertEqual(False, R.And(False, False))


if __name__ == '__main__':
  unittest.main()
