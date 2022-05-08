
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/path.js
"""

deepDict = {
    'a': {
        'b': {
            'c': 'c',
        }
    },
    'falseVal': False,
    'nullVal': None,
    'arrayVal': ['arr'],
}


class TestPathForDict(unittest.TestCase):
  def test_takes_a_path_and_an_object_and_returns_the_value_at_the_path_or_None(self):
    obj = {
        'a': {
            'b': {
                'c': 100,
                'd': 200,
            },
            'e': {
                'f': [100, 101, 102],
                'g': 'G',
            },
            'h': 'H',
        },
        'i': 'I',
        'j': ['J']
    }
    self.assertEqual(100, R.path(['a', 'b', 'c'], obj))
    self.assertEqual(obj, R.path([], obj))
    self.assertEqual(101, R.path(['a', 'e', 'f', 1], obj))
    self.assertEqual('J', R.path(['j', 0], obj))
    self.assertEqual(None, R.path(['j', 1], obj))

  def test_takes_a_path_that_contains_indices_into_arrays(self):
    obj = {
        'a': [[{}], [{'x': 'first'}, {'x': 'second'}, {'x': 'third'}, {'x': 'last'}]]
    }
    self.assertEqual({}, R.path(['a', 0, 0], obj))
    self.assertEqual(None, R.path(['a', 0, 1], obj))
    self.assertEqual('first', R.path(['a', 1, 0, 'x'], obj))
    self.assertEqual('second', R.path(['a', 1, 1, 'x'], obj))
    self.assertEqual('A', R.path([0], ['A']))

  def test_takes_a_path_that_contains_negative_indices_into_arrays(self):
    self.assertEqual('c', R.path(['x', -2], {'x': ['a', 'b', 'c', 'd']}))
    self.assertEqual(97, R.path([-1, 'y'], [{'x': 1, 'y': 99}, {'x': 2, 'y': 98}, {'x': 3, 'y': 97}]))

  def test_gets_a_deep_property_value_from_dicts(self):
    self.assertEqual('c', R.path(['a', 'b', 'c'], deepDict))
    self.assertEqual(deepDict['a'], R.path(['a'], deepDict))

  def test_returns_None_for_items_not_found(self):
    self.assertEqual(None, R.path(['a', 'b', 'foo'], deepDict))
    self.assertEqual(None, R.path(['bar'], deepDict))
    self.assertEqual(None, R.path(['a', 'b'], {'a': None}))


class Obj:
  def __init__(self, a, falseVal, nullVal, arrayVal):
    self.a = a
    self.falseVal = falseVal
    self.nullVal = nullVal
    self.arrayVal = arrayVal


class A:
  def __init__(self, b):
    self.b = b


class B:
  def __init__(self, c):
    self.c = c


b = B('c')
a = A(b)
deepObject = Obj(a, False, None, ['arr'])


class TestPathForObject(unittest.TestCase):
  def test_takes_a_path_and_an_object_and_returns_the_value_at_the_path_or_None(self):
    class Obj:
      def __init__(self, a, i, j):
        self.a = a
        self.i = i
        self.j = j

    class A:
      def __init__(self, b, e, h):
        self.b = b
        self.e = e
        self.h = h

    class B:
      def __init__(self, c, d):
        self.c = c
        self.d = d

    class E:
      def __init__(self, f, g):
        self.f = f
        self.g = g
    b = B(c=100, d=200)
    e = E(f=[100, 101, 102], g='G')
    a = A(b=b, e=e, h='H')
    obj = Obj(a=a, i='I', j=['J'])
    self.assertEqual(100, R.path(['a', 'b', 'c'], obj))
    self.assertEqual(obj, R.path([], obj))
    self.assertEqual(101, R.path(['a', 'e', 'f', 1], obj))
    self.assertEqual('J', R.path(['j', 0], obj))
    self.assertEqual(None, R.path(['j', 1], obj))

  def test_takes_a_path_that_contains_indices_into_arrays(self):
    class Obj:
      def __init__(self, a):
        self.a = a

    class A:
      def __init__(self, x):
        self.x = x
    a = [[{}], [A('first'), A('second'), A('third'), A('last')]]
    obj = Obj(a=a)
    self.assertEqual({}, R.path(['a', 0, 0], obj))
    self.assertEqual(None, R.path(['a', 0, 1], obj))
    self.assertEqual('first', R.path(['a', 1, 0, 'x'], obj))
    self.assertEqual('second', R.path(['a', 1, 1, 'x'], obj))
    self.assertEqual('A', R.path([0], ['A']))

  def test_takes_a_path_that_contains_negative_indices_into_arrays(self):
    class Obj:
      def __init__(self, x):
        self.x = x

    class XY:
      def __init__(self, x, y):
        self.x = x
        self.y = y
    self.assertEqual('c', R.path(['x', -2], Obj(['a', 'b', 'c', 'd'])))
    self.assertEqual(97, R.path([-1, 'y'], [XY(x=1, y=99), XY(x=2, y=98), XY(x=3, y=97)]))

  def test_gets_a_deep_property_value_from_dicts(self):
    self.assertEqual('c', R.path(['a', 'b', 'c'], deepObject))
    self.assertEqual(deepObject.a, R.path(['a'], deepObject))

  def test_returns_None_for_items_not_found(self):
    class A:
      def __init__(self, v):
        self.v = v
    self.assertEqual(None, R.path(['a', 'b', 'foo'], deepObject))
    self.assertEqual(None, R.path(['bar'], deepObject))
    self.assertEqual(None, R.path(['a', 'b'], A(None)))


if __name__ == '__main__':
  unittest.main()
