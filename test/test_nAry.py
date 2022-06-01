
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

  def test_all_arity(self):
    self.assertEqual(0, funcArgsLength(R.nAry(0, toArray)))
    self.assertEqual(1, funcArgsLength(R.nAry(1, toArray)))
    self.assertEqual(2, funcArgsLength(R.nAry(2, toArray)))
    self.assertEqual(3, funcArgsLength(R.nAry(3, toArray)))
    self.assertEqual(4, funcArgsLength(R.nAry(4, toArray)))
    self.assertEqual(5, funcArgsLength(R.nAry(5, toArray)))
    self.assertEqual(6, funcArgsLength(R.nAry(6, toArray)))
    self.assertEqual(7, funcArgsLength(R.nAry(7, toArray)))
    self.assertEqual(8, funcArgsLength(R.nAry(8, toArray)))
    self.assertEqual(9, funcArgsLength(R.nAry(9, toArray)))
    self.assertEqual(10, funcArgsLength(R.nAry(10, toArray)))

    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    self.assertEqual([], R.nAry(0, toArray)(*input))
    self.assertEqual([1], R.nAry(1, toArray)(*input))
    self.assertEqual([1, 2], R.nAry(2, toArray)(*input))
    self.assertEqual([1, 2, 3], R.nAry(3, toArray)(*input))
    self.assertEqual([1, 2, 3, 4], R.nAry(4, toArray)(*input))
    self.assertEqual([1, 2, 3, 4, 5], R.nAry(5, toArray)(*input))
    self.assertEqual([1, 2, 3, 4, 5, 6], R.nAry(6, toArray)(*input))
    self.assertEqual([1, 2, 3, 4, 5, 6, 7], R.nAry(7, toArray)(*input))
    self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], R.nAry(8, toArray)(*input))
    self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], R.nAry(9, toArray)(*input))
    self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], R.nAry(10, toArray)(*input))


if __name__ == '__main__':
  unittest.main()
