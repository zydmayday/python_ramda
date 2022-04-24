
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/lt.js
"""


class TestLt(unittest.TestCase):
  def test_reports_whether_one_item_is_less_than_another(self):
    self.assertEqual(True, R.lt(3, 5))
    self.assertEqual(False, R.lt(6, 5))
    self.assertEqual(False, R.lt(7.0, 7.0))
    self.assertEqual(True, R.lt('abc', 'xyz'))
    self.assertEqual(False, R.lt('abcd', 'abc'))


if __name__ == '__main__':
  unittest.main()
