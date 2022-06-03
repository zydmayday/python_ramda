
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/valuesIn.js
"""


class TestValuesIn(unittest.TestCase):
  def test_returns_an_array_of_the_given_dict_values(self):
    obj = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None}
    vs = R.valuesIn(obj)
    self.assertEqual(5, len(vs))
    self.assertEqual(True, R.indexOf(100, vs) >= 0)
    self.assertEqual(True, R.indexOf('D', vs) >= 0)
    self.assertEqual(True, R.indexOf(None, vs) >= 0)
    self.assertEqual(True, R.indexOf(obj['b'], vs) >= 0)
    self.assertEqual(True, R.indexOf(obj['c'], vs) >= 0)

  def test_returns_an_array_of_the_given_object_values(self):
    class Obj:
      def __init__(self):
        self.a = 100
        self.b = [1, 2, 3]
        self.c = {'x': 200, 'y': 300}
        self.d = 'D'
        self.e = None
    obj = Obj()
    vs = R.valuesIn(obj)
    self.assertEqual(5, len(vs))
    self.assertEqual(True, R.indexOf(100, vs) >= 0)
    self.assertEqual(True, R.indexOf('D', vs) >= 0)
    self.assertEqual(True, R.indexOf(None, vs) >= 0)
    self.assertEqual(True, R.indexOf(obj.b, vs) >= 0)
    self.assertEqual(True, R.indexOf(obj.c, vs) >= 0)

  def test_works_with_parent_class(self):
    class Parent:
      ps = 'parent static'

      def __init__(self):
        self.p = 'parent local'

    class Child(Parent):
      cs = 'child static'

      def __init__(self):
        super().__init__()
        self.c = 'child local'

    obj = Child()
    vs = R.valuesIn(obj)
    self.assertEqual(4, len(vs))
    self.assertEqual(True, R.indexOf('parent static', vs) >= 0)
    self.assertEqual(True, R.indexOf('parent local', vs) >= 0)
    self.assertEqual(True, R.indexOf('child static', vs) >= 0)
    self.assertEqual(True, R.indexOf('child local', vs) >= 0)

  def test_works_for_primitives(self):
    self.assertEqual([], R.valuesIn(None))
    self.assertEqual([], R.valuesIn(55))
    self.assertEqual([], R.valuesIn(True))
    self.assertEqual([], R.valuesIn(False))
    self.assertEqual([], R.valuesIn([]))
    self.assertEqual([], R.valuesIn(''))


if __name__ == '__main__':
  unittest.main()
