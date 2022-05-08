
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/paths.js
"""

d = {
    'a': {

        'b': {
            'c': 1,
            'd': 2,
        }
    },
    'p': [{'q': 3}, 'Hi'],
    'x': {
        'y': 'Alice',
        'z': [[{}]]
    }
}


class TestPathsForDict(unittest.TestCase):
  def test_takes_paths_and_returns_values_at_those_paths(self):
    self.assertEqual([1, 'Alice'], R.paths([['a', 'b', 'c'], ['x', 'y']], d))
    self.assertEqual([2, None], R.paths([['a', 'b', 'd'], ['p', 'q']], d))

  def test_takes_a_paths_that_contains_indices_into_arrays(self):
    self.assertEqual([3, {}], R.paths([['p', 0, 'q'], ['x', 'z', 0, 0]], d))
    self.assertEqual([3, None], R.paths([['p', 0, 'q'], ['x', 'z', 2, 1]], d))

  def test_takes_a_paths_that_contains_negative_indices_into_array(self):
    self.assertEqual([3, 'Hi'], R.paths([['p', -2, 'q'], ['p', -1]], d))
    self.assertEqual([None, {}], R.paths([['p', -4, 'q'], ['x', 'z', -1, 0]], d))

  def test_gets_a_deep_property_value_from_dicts(self):
    self.assertEqual([d['a']['b']], R.paths([['a', 'b']], d))
    self.assertEqual([d['p'][0]], R.paths([['p', 0]], d))

  def test_returns_None_for_items_not_found(self):
    self.assertEqual([None], R.paths([['a', 'x', 'y']], d))
    self.assertEqual([None], R.paths([['p', 2]], d))


class Obj:
  def __init__(self, a, p, x):
    self.a = a
    self.p = p
    self.x = x


class A:
  def __init__(self, b):
    self.b = b


class B:
  def __init__(self, c, d):
    self.c = c
    self.d = d


class Q:
  def __init__(self, q):
    self.q = q


class X:
  def __init__(self, y, z):
    self.y = y
    self.z = z


b = B(c=1, d=2)
a = A(b=b)
q = Q(q=3)
p = [q, 'Hi']
x = X(y='Alice', z=[[{}]])
obj = Obj(a=a, p=p, x=x)


class TestPathsForObject(unittest.TestCase):
  def test_takes_paths_and_returns_values_at_those_paths(self):
    self.assertEqual([1, 'Alice'], R.paths([['a', 'b', 'c'], ['x', 'y']], obj))
    self.assertEqual([2, None], R.paths([['a', 'b', 'd'], ['p', 'q']], obj))

  def test_takes_a_paths_that_contains_indices_into_arrays(self):
    self.assertEqual([3, {}], R.paths([['p', 0, 'q'], ['x', 'z', 0, 0]], obj))
    self.assertEqual([3, None], R.paths([['p', 0, 'q'], ['x', 'z', 2, 1]], obj))

  def test_takes_a_paths_that_contains_negative_indices_into_array(self):
    self.assertEqual([3, 'Hi'], R.paths([['p', -2, 'q'], ['p', -1]], obj))
    self.assertEqual([None, {}], R.paths([['p', -4, 'q'], ['x', 'z', -1, 0]], obj))

  def test_gets_a_deep_property_value_from_objects(self):
    self.assertEqual([obj.a.b], R.paths([['a', 'b']], obj))
    self.assertEqual([obj.p[0]], R.paths([['p', 0]], obj))

  def test_returns_None_for_items_not_found(self):
    self.assertEqual([None], R.paths([['a', 'x', 'y']], obj))
    self.assertEqual([None], R.paths([['p', 2]], obj))


if __name__ == '__main__':
  unittest.main()
