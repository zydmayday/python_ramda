
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/or.js
"""


class TestOr(unittest.TestCase):
  def test_compares_two_values_with_python_or(self):
    self.assertEqual(True, R.Or(True, True))
    self.assertEqual(True, R.Or(True, False))
    self.assertEqual(True, R.Or(False, True))
    self.assertEqual(False, R.Or(False, False))


if __name__ == '__main__':
  unittest.main()
