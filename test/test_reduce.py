
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/reduce.js
"""


def add(a, b): return a + b
def mult(a, b): return a * b


def gen_int():
  yield 1
  yield 2
  yield 3
  yield 4


class ReduceObj:
  def reduce(self, step, acc):
    return 'override'


class TestReduce(unittest.TestCase):
  def test_folds_simple_functions_over_arrays_with_the_supplied_accumulator(self):
    self.assertEqual(10, R.reduce(add, 0, [1, 2, 3, 4]))
    self.assertEqual(24, R.reduce(mult, 1, [1, 2, 3, 4]))

  def test_dispatches_to_objects_that_implement_reduce(self):
    obj = ReduceObj()
    self.assertEqual('override', R.reduce(add, 0, obj))
    self.assertEqual('override', R.reduce(add, 10, obj))

  def test_returns_the_accumulator_for_an_empty_array(self):
    self.assertEqual(0, R.reduce(add, 0, []))
    self.assertEqual(1, R.reduce(mult, 1, []))
    self.assertEqual([], R.reduce(R.concat, [], []))

  def test_returns_the_accumulator_for_an_None_list(self):
    self.assertEqual(0, R.reduce(add, 0, None))
    self.assertEqual([], R.reduce(R.concat, [], None))

  def test_short_circuits_with_reduced(self):
    def addWithMaxOf10(acc, val): return R.reduced(acc) if acc + val > 10 else acc + val
    self.assertEqual(10, R.reduce(addWithMaxOf10, 0, [1, 2, 3, 4]))
    self.assertEqual(6, R.reduce(addWithMaxOf10, 0, [2, 4, 6, 8]))


class TestPythonStyleReduce(unittest.TestCase):
  def test_with_yield(self):
    self.assertEqual(10, R.reduce(add, 0, gen_int()))
    self.assertEqual(24, R.reduce(mult, 1, gen_int()))


if __name__ == '__main__':
  unittest.main()
