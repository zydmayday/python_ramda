
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/nAry.js
"""


def toArray(*args):
  return list(args)


class TestNAry(unittest.TestCase):
  def test_turns_multiple_argument_function_into_a_nullary_one(self):
    fn = R.nAry(0, toArray)
    self.assertEqual(0, funcArgsLength(fn))
    self.assertEqual([], fn(1, 2, 3))

  def test_turns_multiple_argument_function_into_a_ternary_one(self):
    fn = R.nAry(3, toArray)
    self.assertEqual(3, funcArgsLength(fn))
    self.assertEqual([1, 2, 3], fn(1, 2, 3, 4))
    self.assertEqual([1, None, None], fn(1))

  def test_creates_functions_of_arity_less_than_or_equal_to_ten(self):
    fn = R.nAry(10, toArray)
    self.assertEqual(10, funcArgsLength(fn))
    self.assertEqual(R.range(0, 10), fn(*R.range(0, 25)))

    nones = fn()
    ns = R.repeat(None, 10)
    self.assertEqual(nones, ns)

  def test_throws_if_n_is_greater_than_ten(self):
    with self.assertRaises(ValueError):
      R.nAry(11, toArray)

if __name__ == '__main__':
  unittest.main()
