
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/binary.js
"""


class TestBinary(unittest.TestCase):
  def test_turns_multiple_argument_function_into_binary_one(self):
    fn = R.binary(lambda *args: list(args))
    self.assertEqual(2, funcArgsLength(fn))
    self.assertEqual([10, 20], fn(10, 20))


if __name__ == '__main__':
  unittest.main()
