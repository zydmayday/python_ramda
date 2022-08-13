
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/inc.js
"""


class TestInc(unittest.TestCase):
  def test_increments_its_argument(self):
    self.assertEqual(0, R.inc(-1))
    self.assertEqual(1, R.inc(0))
    self.assertEqual(2, R.inc(1))
    self.assertEqual(13.34, R.inc(12.34))
    self.assertEqual(float('-inf'), R.inc(float('-inf')))
    self.assertEqual(float('inf'), R.inc(float('inf')))


if __name__ == '__main__':
  unittest.main()
