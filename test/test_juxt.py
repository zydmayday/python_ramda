
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/juxt.js
"""


def hello():
  return "hello"


def bye():
  return "bye"


class TestJuxt(unittest.TestCase):
  def test_works_with_no_functions_and_no_values(self):
    self.assertEqual([], R.juxt([])())

  def test_works_with_no_functions_and_some_values(self):
    self.assertEqual([], R.juxt([])(2, 3))

  def test_works_with_1_function_and_no_values(self):
    self.assertEqual(['hello'], R.juxt([hello])())

  def test_works_with_1_function_and_1_value(self):
    self.assertEqual([5], R.juxt([R.add(3)])(2))

  def test_works_with_1_function_and_some_value(self):
    self.assertEqual([6], R.juxt([R.multiply])(2, 3))

  def test_works_with_some_functions_and_no_value(self):
    self.assertEqual(['hello', 'bye'], R.juxt([hello, bye])())

  def test_works_with_some_functions_and_1_value(self):
    self.assertEqual([4, 5], R.juxt([R.multiply(2), R.add(3)])(2))

  def test_works_with_some_functions_and_some_value(self):
    self.assertEqual([5, 6], R.juxt([R.add, R.multiply])(2, 3))

  def test_retains_the_highest_arity(self):
    f = R.juxt([R.nAry(1, R.T), R.nAry(3, R.T), R.nAry(2, R.T)])
    self.assertEqual(3, funcArgsLength(f))

  def test_returns_a_curried_function(self):
    self.assertEqual([6, 5], R.juxt([R.multiply, R.add])(2)(3))


if __name__ == '__main__':
  unittest.main()
