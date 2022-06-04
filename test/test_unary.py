
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/unary.js
"""


class TestUnary(unittest.TestCase):
  def test_turns_multiple_argument_function_into_unary_one(self):
    fn = R.unary(lambda *args: list(args))
    self.assertEqual(1, funcArgsLength(fn))
    self.assertEqual([1], fn(1, 2, 3))


if __name__ == '__main__':
  unittest.main()
