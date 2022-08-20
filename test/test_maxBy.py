import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/maxBy.js
"""


class TestMaxBy(unittest.TestCase):
  def test_returns_the_larger_value_as_determined_by_the_function(self):
    self.assertEqual(-3, R.maxBy(lambda x: x * x, -3, 2))
    self.assertEqual({'x': 5, 'y': 10}, R.maxBy(R.prop('x'), {'x': 3, 'y': 1}, {'x': 5, 'y': 10}))


if __name__ == '__main__':
  unittest.main()
