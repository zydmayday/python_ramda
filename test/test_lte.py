
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/lte.js
"""


class TestLte(unittest.TestCase):
  def test_reports_whether_one_item_is_less_than_or_equal_to_another(self):
    self.assertEqual(True, R.lte(3, 5))
    self.assertEqual(False, R.lte(6, 5))
    self.assertEqual(True, R.lte(7.0, 7.0))
    self.assertEqual(True, R.lte('abc', 'xyz'))
    self.assertEqual(False, R.lte('abcd', 'abc'))


if __name__ == '__main__':
  unittest.main()
