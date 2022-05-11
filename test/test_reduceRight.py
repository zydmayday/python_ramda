
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/reduceRight.js
"""


def avg(a, b): return (a + b) / 2


def concatFirstThree(val, acc): return R.reduced(acc) if len(acc) == 3 else R.concat(acc, val)


class TestReduceRight(unittest.TestCase):
  def test_folds_lists_in_the_right_order(self):
    self.assertEqual('abcd', R.reduceRight(lambda a, b: a + b, '', ['a', 'b', 'c', 'd']))

  def test_folds_subtract_over_arrays_in_the_right_order(self):
    self.assertEqual(-2, R.reduceRight(lambda a, b: a - b, 0, [1, 2, 3, 4]))

  def test_folds_simple_functions_over_arrays_with_the_supplied_accumulator(self):
    self.assertEqual(12, R.reduceRight(avg, 54, [12, 4, 10, 6]))

  def test_returns_the_accumulator_for_an_empty_array(self):
    self.assertEqual(0, R.reduceRight(avg, 0, []))

  def test_short_circuits_with_reduced(self):
    self.assertEqual('ram', R.reduceRight(concatFirstThree, '', ['a', 'd', 'm', 'a', 'r']))


if __name__ == '__main__':
  unittest.main()
