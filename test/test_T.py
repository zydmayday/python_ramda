
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/T.js
"""


class TestT(unittest.TestCase):
  def test_always_returns_true(self):
    self.assertEqual(True, R.T())
    self.assertEqual(True, R.T(10))
    self.assertEqual(True, R.T(True))


if __name__ == '__main__':
  unittest.main()
