
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/props.js
"""

d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
}


class TestPropsForDict(unittest.TestCase):
  def test_returns_empty_array_if_no_properties_requested(self):
    self.assertEqual([], R.props([], d))

  def test_returns_values_for_requested_properties(self):
    self.assertEqual([1, 5], R.props(['a', 'e'], d))

  def test_preserves_order(self):
    self.assertEqual([6, 3, 5], R.props(['f', 'c', 'e'], d))

  def test_returns_None_for_nonexistent_properties(self):
    ps = R.props(['a', 'nonexistent'], d)
    self.assertEqual(2, len(ps))
    self.assertEqual(1, ps[0])
    self.assertEqual(None, ps[1])

class Obj:
  def __init__(self, a, b, c, d, e, f):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e
    self.f = f
obj = Obj(1, 2, 3, 4, 5, 6)

class TestPropsForObject(unittest.TestCase):
  def test_returns_empty_array_if_no_properties_requested(self):
    self.assertEqual([], R.props([], obj))

  def test_returns_values_for_requested_properties(self):
    self.assertEqual([1, 5], R.props(['a', 'e'], obj))

  def test_preserves_order(self):
    self.assertEqual([6, 3, 5], R.props(['f', 'c', 'e'], obj))

  def test_returns_None_for_nonexistent_properties(self):
    ps = R.props(['a', 'nonexistent'], obj)
    self.assertEqual(2, len(ps))
    self.assertEqual(1, ps[0])
    self.assertEqual(None, ps[1])

if __name__ == '__main__':
  unittest.main()
