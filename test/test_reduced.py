
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/reduced.js
"""


class TestReduced(unittest.TestCase):
  def test_wraps_a_value(self):
    v = {}
    self.assertEqual(v, R.reduced(v)['@@transducer/value'])

  def test_flags_value_as_reduced(self):
    self.assertEqual(True, R.reduced({})['@@transducer/reduced'])

  def test_short_circuits_reduced(self):
    def fn(acc, v):
      result = acc + v
      if result >= 10:
        result = R.reduced(result)
      return result
    self.assertEqual(10, R.reduce(fn, 0, [1, 2, 3, 4, 5]))


if __name__ == '__main__':
  unittest.main()
