
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/construct.js
"""


class Rectangle:
  def __init__(self, w, h):
    self.w = w
    self.h = h

  def area(self):
    return self.w * self.h


class TestConstruct(unittest.TestCase):
  def test_returns_a_constructor_function_into_one_that_can_be_called_without_new(self):
    rect = R.construct(Rectangle)
    r1 = rect(3, 4)
    self.assertEqual(3, r1.w)
    self.assertEqual(12, r1.area())

  def test_supports_constructors_with_no_arguments(self):
    class Foo:
      pass
    foo = R.construct(Foo)
    self.assertIsInstance(foo(), Foo)

  def test_does_not_support_constructors_with_more_than_ten_arguments(self):
    class Foo:
      def __init__(self, a, b, c, d, e, f, g, h, i, j, k):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
    with self.assertRaises(ValueError):
      R.construct(Foo)

  def test_returns_a_curried_function(self):
    rect = R.construct(Rectangle)
    r1 = rect(3)(4)
    self.assertEqual(3, r1.w)
    self.assertEqual(12, r1.area())

if __name__ == '__main__':
  unittest.main()
