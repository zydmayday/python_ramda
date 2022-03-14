import unittest

import pamda as R
from pamda.private._curry2 import _curry2

"""
https://github.com/ramda/ramda/blob/master/test/internal/_curry2.js
"""


class Test_Curry2(unittest.TestCase):
  def test_supports_placeholder(self):
    def f(a, b): return [a, b]
    g = _curry2(f)
    self.assertEqual([1, 2], g(1)(2))
    self.assertEqual([1, 2], g(1, 2))

    self.assertEqual([1, 2], g(R.__, 2)(1))
    self.assertEqual([1, 2], g(1, R.__)(2))

    self.assertEqual([1, 2], g(R.__, R.__)(1)(2))
    self.assertEqual([1, 2], g(R.__, R.__)(1, 2))
    self.assertEqual([1, 2], g(R.__, R.__)(R.__)(1, 2))
    self.assertEqual([1, 2], g(R.__, R.__)(R.__, 2)(1))


if __name__ == '__main__':
  unittest.main()
