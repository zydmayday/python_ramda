
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/times.js
"""


class TestTimes(unittest.TestCase):
  def test_takes_a_map_func(self):
    self.assertEqual([0, 1, 2, 3, 4], R.times(R.identity, 5))
    self.assertEqual([0, 2, 4, 6, 8], R.times(R.multiply(2), 5))

  def test_throws_if_second_argument_is_not_a_valid_array_length(self):
    with self.assertRaises(ValueError):
      R.times(3)('cheers!')
    with self.assertRaises(ValueError):
      R.times(R.identity, -1)


if __name__ == '__main__':
  unittest.main()
