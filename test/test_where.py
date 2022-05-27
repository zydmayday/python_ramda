
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/where.js
"""


class TestWhereForDict(unittest.TestCase):
  def test_returns_true_if_the_test_dict_satisfies_the_spec(self):
    spec = {'x': R.equals(1), 'y': R.equals(2)}
    test1 = {'x': 0, 'y': 200}
    test2 = {'x': 0, 'y': 10}
    test3 = {'x': 1, 'y': 101}
    test4 = {'x': 1, 'y': 2}
    self.assertEqual(False, R.where(spec, test1))
    self.assertEqual(False, R.where(spec, test2))
    self.assertEqual(False, R.where(spec, test3))
    self.assertEqual(True, R.where(spec, test4))

  def test_does_not_need_the_spec_and_the_test_object_to_have_the_same_interface(self):
    spec = {'x': R.equals(100)}
    test1 = {'x': 20, 'y': 100, 'z': 100}
    test2 = {'w': 1, 'x': 100, 'y': 100, 'z': 100}

    self.assertEqual(False, R.where(spec, test1))
    self.assertEqual(True, R.where(spec, test2))

  def test_matches_specs_that_have_None_properties(self):
    spec = {'x': R.equals(None)}
    test1 = {}
    test2 = {'x': None}
    test3 = {'x': 1}

    self.assertEqual(True, R.where(spec, test1))
    self.assertEqual(True, R.where(spec, test2))
    self.assertEqual(False, R.where(spec, test3))

class TestWhereForObject(unittest.TestCase):
  def test_returns_true_if_the_test_dict_satisfies_the_spec(self):
    class Test:
      def __init__(self, x, y):
        self.x = x
        self.y = y
    spec = {'x': R.equals(1), 'y': R.equals(2)}
    test1 = Test(0, 200)
    test2 = Test(0, 10)
    test3 = Test(1, 101)
    test4 = Test(1, 2)
    self.assertEqual(False, R.where(spec, test1))
    self.assertEqual(False, R.where(spec, test2))
    self.assertEqual(False, R.where(spec, test3))
    self.assertEqual(True, R.where(spec, test4))

  def test_does_not_need_the_spec_and_the_test_object_to_have_the_same_interface(self):
    class Test1:
      def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    class Test2:
      def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    spec = {'x': R.equals(100)}
    test1 = Test1(20, 100, 100)
    test2 = Test2(1, 100, 100, 100)

    self.assertEqual(False, R.where(spec, test1))
    self.assertEqual(True, R.where(spec, test2))

  def test_matches_specs_that_have_None_properties(self):
    class Test1:
      def __init__(self):
        pass

    class Test2:
      def __init__(self, x):
        self.x = x

    spec = {'x': R.equals(None)}
    test1 = Test1()
    test2 = Test2(None)
    test3 = Test2(1)

    self.assertEqual(True, R.where(spec, test1))
    self.assertEqual(True, R.where(spec, test2))
    self.assertEqual(False, R.where(spec, test3))

  def test_is_true_for_an_empty_spec(self):
    class Test:
      def __init__(self, a):
        self.a = a

    self.assertEqual(True, R.where({}, Test(1)))

  def test_matches_super_class_property_if_super_init_called(self):
    class Parent:
      def __init__(self):
        self.x = 1

    class Child(Parent):
      def __init__(self):
        super().__init__()
        self.y = 2

    spec1 = {'x': R.equals(1)}
    spec2 = {'y': R.equals(2)}

    self.assertEqual(True, R.where(spec1, Child()))
    self.assertEqual(True, R.where(spec1, Parent()))
    self.assertEqual(True, R.where(spec2, Child()))
    self.assertEqual(False, R.where(spec2, Parent()))


if __name__ == '__main__':
  unittest.main()
