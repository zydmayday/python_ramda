
import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/pathEq.js
"""

dictObj = {
    'a': 1,
    'b': [{
        'ba': 2,
    }, {
        'ba': 3
    }]
}


class Obj:
  def __init__(self, a, b):
    self.a = a
    self.b = b


class Ba:
  def __init__(self, ba):
    self.ba = ba


obj = Obj(1, [Ba(2), Ba(3)])


class TestPathEqForDict(unittest.TestCase):
  def test_returns_true_if_the_path_matches_the_value(self):
    self.assertEqual(True, R.pathEq(1, ['a'], dictObj))
    self.assertEqual(True, R.pathEq(3, ['b', 1, 'ba'], dictObj))

  def test_returns_false_for_non_matches(self):
    self.assertEqual(False, R.pathEq('1', ['a'], dictObj))
    self.assertEqual(False, R.pathEq(3, ['b', 0, 'ba'], dictObj))

  def test_returns_false_for_non_existing_values(self):
    self.assertEqual(False, R.pathEq('foo', ['c'], dictObj))
    self.assertEqual(False, R.pathEq('foo', ['c', 'd'], dictObj))

  def test_accepts_empty_path(self):
    self.assertEqual(False, R.pathEq(42, [], {'a': 1, 'b': 2}))
    self.assertEqual(True, R.pathEq(dictObj, [], dictObj))

class TestPathEqForObject(unittest.TestCase):
  def test_returns_true_if_the_path_matches_the_value(self):
    self.assertEqual(True, R.pathEq(1, ['a'], obj))
    self.assertEqual(True, R.pathEq(3, ['b', 1, 'ba'], obj))

  def test_returns_false_for_non_matches(self):
    self.assertEqual(False, R.pathEq('1', ['a'], obj))
    self.assertEqual(False, R.pathEq(3, ['b', 0, 'ba'], obj))

  def test_returns_false_for_non_existing_values(self):
    self.assertEqual(False, R.pathEq('foo', ['c'], obj))
    self.assertEqual(False, R.pathEq('foo', ['c', 'd'], obj))

  def test_accepts_empty_path(self):
    self.assertEqual(False, R.pathEq(42, [], {'a': 1, 'b': 2}))
    self.assertEqual(True, R.pathEq(obj, [], obj))

class TestPathEqForOthers(unittest.TestCase):
  def test_has_R_equals_semantics(self):
    self.assertEqual(False, R.pathEq(0.0, ['value'], {'value': -0.0}))
    self.assertEqual(False, R.pathEq(-0.0, ['value'], {'value': 0.0}))
    self.assertEqual(True, R.pathEq(float('nan'), ['value'], {'value': float('nan')}))
    self.assertEqual(True, R.pathEq(Just([42]), ['value'], {'value': Just([42])}))


if __name__ == '__main__':
  unittest.main()
