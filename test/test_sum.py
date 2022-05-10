
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/sum.js
"""


class TestSum(unittest.TestCase):
  def test_adds_together_the_array_of_numbers_supplied(self):
    self.assertEqual(10, R.sum([1, 2, 3, 4]))

  def test_does_not_save_the_state_of_the_accumulator(self):
    self.assertEqual(10, R.sum([1, 2, 3, 4]))
    self.assertEqual(1, R.sum([1]))
    self.assertEqual(25, R.sum([5, 5, 5, 5, 5]))

if __name__ == '__main__':
  unittest.main()
