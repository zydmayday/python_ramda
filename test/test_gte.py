
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/gte.js
"""


class TestGte(unittest.TestCase):
  def test_reports_whether_one_item_is_greater_than_or_equal_to_another(self):
    self.assertEqual(False, R.gte(3, 5))
    self.assertEqual(True, R.gte(6, 5))
    self.assertEqual(True, R.gte(7.0, 7.0))
    self.assertEqual(False, R.gte('abc', 'xyz'))
    self.assertEqual(True, R.gte('abcd', 'abc'))


if __name__ == '__main__':
  unittest.main()
