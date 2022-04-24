
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/gt.js
"""


class TestGt(unittest.TestCase):
  def test_reports_whether_one_item_is_greater_than_another(self):
    self.assertEqual(False, R.gt(3, 5))
    self.assertEqual(True, R.gt(6, 5))
    self.assertEqual(False, R.gt(7.0, 7.0))
    self.assertEqual(False, R.gt('abc', 'xyz'))
    self.assertEqual(True, R.gt('abcd', 'abc'))


if __name__ == '__main__':
  unittest.main()
