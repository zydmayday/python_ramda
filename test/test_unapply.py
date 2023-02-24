
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/unapply.js
"""


class TestLt(unittest.TestCase):
  def test_returns_a_function_which_is_always_passed_one_argument(self):
    fn = R.unapply(lambda *args: len(args))

    self.assertEqual(1, fn())
    self.assertEqual(1, fn('x'))
    self.assertEqual(1, fn('x', 'y'))
    self.assertEqual(1, fn('x', 'y', 'z'))

  def test_forwards_arguments_to_decorated_function_as_an_array(self):
    fn = R.unapply(lambda xs: str(xs))

    self.assertEqual('[]', fn())
    self.assertEqual('[2]', fn(2))
    self.assertEqual('[2, 4]', fn(2, 4))
    self.assertEqual('[2, 4, 6]', fn(2, 4, 6))

  def test_returns_a_function_with_length_0(self):
    fn = R.unapply(R.identity)
    self.assertEqual(0, funcArgsLength(fn))

  def test_is_the_inverse_of_R_apply(self):
    f = R.Max
    g = R.unapply(R.apply(f))
    self.assertEqual(f(1, 2, 3), g(1, 2, 3))


if __name__ == '__main__':
  unittest.main()
