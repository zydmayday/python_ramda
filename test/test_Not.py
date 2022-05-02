
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/not.js
"""


class TestNot(unittest.TestCase):
  def test_reverses_argument(self):
    self.assertEqual(True, R.Not(False))
    self.assertEqual(False, R.Not(1))
    self.assertEqual(True, R.Not(''))


if __name__ == '__main__':
  unittest.main()
