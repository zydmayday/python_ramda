
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/keysIn.js
"""


class TestKeysIn(unittest.TestCase):
  def test_returns_an_array_of_the_given_dict_keys(self):
    d = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None}
    self.assertEqual(['a', 'b', 'c', 'd', 'e'], R.keysIn(d))

  def test_returns_an_array_of_the_given_obj_keys(self):
    class Obj:
      def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
    obj = Obj(100, [1, 2, 3], {'x': 200, 'y': 300}, 'D', None)
    self.assertEqual(['a', 'b', 'c', 'd', 'e'], R.keysIn(obj))

  def test_returns_an_array_of_the_given_obj_with_parent_keys(self):
    class Parent:
      ps1 = 'parent static 1'
      ps2 = 'parent static 2'

      def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    class Child(Parent):
      cs1 = 'child static 1'
      cs2 = 'child static 2'

      def __init__(self, p1, p2, c1, c2):
        super().__init__(p1, p2)
        self.c1 = c1
        self.c2 = c2

    child = Child('p1', 'p2', 'c1', 'c2')
    self.assertEqual(['cs1', 'cs2', 'ps1', 'ps2', 'p1', 'p2', 'c1', 'c2'], R.keysIn(child))

  def test_works_for_primitives(self):
    self.assertEqual([], R.keysIn(None))
    self.assertEqual([], R.keysIn(0))
    self.assertEqual([], R.keysIn(False))
    self.assertEqual([], R.keysIn(True))
    self.assertEqual([], R.keysIn(''))
    self.assertEqual([], R.keysIn([]))
    self.assertEqual([], R.keysIn({}))


if __name__ == '__main__':
  unittest.main()
