
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/F.js
"""


class TestF(unittest.TestCase):
  def test_always_returns_false(self):
    self.assertEqual(False, R.F())
    self.assertEqual(False, R.F(10))
    self.assertEqual(False, R.F(True))


if __name__ == '__main__':
  unittest.main()
