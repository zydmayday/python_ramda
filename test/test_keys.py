
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/keys.js
"""

obj = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None}


class A:
  def __init__(self):
    self.a = 'a'


class B(A):
  def __init__(self):
    self.b = 'b'


class C(A):
  def __init__(self):
    super().__init__()
    self.c = 'c'


class TestKeys(unittest.TestCase):
  def test_returns_an_array_of_the_given_object_own_keys(self):
    self.assertEqual(['a', 'b', 'c', 'd', 'e'], R.keys(obj))

  def test_works_with_attribute_override(self):
    a, b, c = A(), B(), C()
    self.assertEqual(['a'], R.keys(a))
    self.assertEqual(['b'], R.keys(b))
    self.assertEqual(['a', 'c'], R.keys(c))

  def test_works_with_primitives(self):
    self.assertEqual([], R.keys(None))
    self.assertEqual([], R.keys(55))
    self.assertEqual([], R.keys('foo'))
    self.assertEqual([], R.keys(True))
    self.assertEqual([], R.keys(False))
    self.assertEqual([], R.keys([]))
    self.assertEqual([], R.keys({}))

  def test_works_with_methods_properties(self):
    self.assertEqual(['foo'], R.keys({'foo': lambda x: x}))

    # keys does not work with methods in object


if __name__ == '__main__':
  unittest.main()
