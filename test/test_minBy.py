
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/minBy.js
"""


class TestMinBy(unittest.TestCase):
  def test_returns_the_smaller_value_as_determined_by_the_function(self):
    self.assertEqual(2, R.minBy(lambda x: x * x, -3, 2))
    self.assertEqual({'x': 3, 'y': 1}, R.minBy(R.prop('x'), {'x': 3, 'y': 1}, {'x': 5, 'y': 10}))


if __name__ == '__main__':
  unittest.main()
