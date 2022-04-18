import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/nth.js
"""

arr = ['foo', 'bar', 'baz', 'quux']


class TestNth(unittest.TestCase):
  def test_accepts_positive_offsets(self):
    self.assertEqual('foo', R.nth(0, arr))
    self.assertEqual('bar', R.nth(1, arr))
    self.assertEqual('baz', R.nth(2, arr))
    self.assertEqual('quux', R.nth(3, arr))
    self.assertEqual(None, R.nth(4, arr))

    self.assertEqual('a', R.nth(0, 'abc'))
    self.assertEqual('b', R.nth(1, 'abc'))
    self.assertEqual('c', R.nth(2, 'abc'))
    self.assertEqual('', R.nth(3, 'abc'))

  def test_accepts_negative_offsets(self):
    self.assertEqual('foo', R.nth(-4, arr))
    self.assertEqual('bar', R.nth(-3, arr))
    self.assertEqual('baz', R.nth(-2, arr))
    self.assertEqual('quux', R.nth(-1, arr))
    self.assertEqual(None, R.nth(-5, arr))

    self.assertEqual('a', R.nth(-3, 'abc'))
    self.assertEqual('b', R.nth(-2, 'abc'))
    self.assertEqual('c', R.nth(-1, 'abc'))
    self.assertEqual('', R.nth(-4, 'abc'))

  def test_throws_if_applied_to_None(self):
    with self.assertRaises(TypeError):
      R.nth(0, None)


if __name__ == '__main__':
  unittest.main()
