
import unittest

import pamda as R

"""
https://github.com/ramda/ramda/blob/master/test/reduce.js
"""


def add(a, b): return a + b
def mult(a, b): return a * b


class TestReduce(unittest.TestCase):
  def test_folds_simple_functions_over_arrays_with_the_supplied_accumulator(self):
    self.assertEqual(10, R.reduce(add, 0, [1, 2, 3, 4]))
    self.assertEqual(24, R.reduce(mult, 1, [1, 2, 3, 4]))

  def test_returns_the_accumulator_for_an_empty_array(self):
    self.assertEqual(0, R.reduce(add, 0, []))
    self.assertEqual(1, R.reduce(mult, 1, []))
    # TODO: add test case for concat

  def test_returns_the_accumulator_for_an_None_list(self):
    self.assertEqual(0, R.reduce(add, 0, None))
    # TODO: add test case for concat

  # TODO: add other types of test

if __name__ == '__main__':
  unittest.main()
