
import unittest

from ramda.private._helper import isNegativeFloatZero


class Test_Helper(unittest.TestCase):
  def test_isNegativeZero(self):
    self.assertEqual(True, isNegativeFloatZero(-0.0))
    self.assertEqual(False, isNegativeFloatZero(-0))
    self.assertEqual(False, isNegativeFloatZero(0))
    self.assertEqual(False, isNegativeFloatZero(0.0))
    self.assertEqual(False, isNegativeFloatZero(-0.1))
    self.assertEqual(False, isNegativeFloatZero(0.1))


if __name__ == '__main__':
  unittest.main()
