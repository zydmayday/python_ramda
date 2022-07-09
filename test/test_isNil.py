
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/isNil.js
"""


class TestIsNil(unittest.TestCase):
  def test_a_value_for_None(self):
    self.assertEqual(True, R.isNil(None))
    self.assertEqual(False, R.isNil([]))
    self.assertEqual(False, R.isNil({}))
    self.assertEqual(False, R.isNil(0))
    self.assertEqual(False, R.isNil(''))


if __name__ == '__main__':
  unittest.main()
