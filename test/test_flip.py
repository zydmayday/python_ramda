
import unittest

import ramda as R
from ramda.private._inspect import funcArgsLength

"""
https://github.com/ramda/ramda/blob/master/test/flip.js
"""


class TestFlip(unittest.TestCase):
  def test_returns_a_function_which_inverts_the_first_two_arguments_to_the_supplied_function(self):
    def f(a, b, c): return f'{a} {b} {c}'
    g = R.flip(f)
    self.assertEqual('a b c', f('a', 'b', 'c'))
    self.assertEqual('b a c', g('a', 'b', 'c'))

  def test_returns_a_curried_function(self):
    def f(a, b, c): return f'{a} {b} {c}'
    g = R.flip(f)('a')
    self.assertEqual('b a c', g('b', 'c'))

  def test_returns_a_function_with_correct_arity(self):
    def f2(a, b): return f'{a} {b}'
    def f3(a, b, c): return f'{a} {b} {c}'
    self.assertEqual(2, funcArgsLength(R.flip(f2)))
    self.assertEqual(3, funcArgsLength(R.flip(f3)))


class TestFlipProperties(unittest.TestCase):
  def test_inverts_first_two_arguments(self):
    def f(a, b, c): return f'{a} {b} {c}'
    g = R.flip(f)
    self.assertEqual(g('b', 'a', 'c'), f('a', 'b', 'c'))


if __name__ == '__main__':
  unittest.main()
