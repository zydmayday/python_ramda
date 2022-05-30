
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength
from ramda.private._isFunction import _isFunction

"""
https://github.com/ramda/ramda/blob/master/test/useWith.js
"""

add1 = R.add(1)
mult2 = R.multiply(2)
div3 = R.divide(R.__, 3)
f = R.useWith(max, [add1, mult2, div3])


class TestUseWith(unittest.TestCase):
  def test_takes_a_list_of_function_and_returns_a_function(self):
    self.assertTrue(_isFunction(R.useWith(max, [])))
    self.assertTrue(_isFunction(R.useWith(max, [add1])))
    self.assertTrue(_isFunction(R.useWith(max, [add1, mult2, div3])))

  def test_passes_the_arguments_received_to_their_respective_functions(self):
    self.assertEqual(16, f(7, 8, 9))

  def test_passes_additional_arguments_to_the_main_function(self):
    self.assertEqual(16, f(7, 8, 9, 10))
    self.assertEqual(20, f(7, 8, 9, 20))

  def test_has_the_correct_arity(self):
    self.assertEqual(3, funcArgsLength(f))


if __name__ == '__main__':
  unittest.main()
