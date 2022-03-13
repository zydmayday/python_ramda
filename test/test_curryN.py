
import unittest

from pamda import curryN


def source(a, b, c):
  return a * b * c

'''
https://github.com/ramda/ramda/blob/master/test/curryN.js
'''
class TestCurry(unittest.TestCase):

  def test_accepts_an_arity(self):
    curried = curryN(3, source)
    self.assertEqual(6, curried(1)(2)(3))
    self.assertEqual(6, curried(1, 2)(3))
    self.assertEqual(6, curried(1)(2, 3))
    self.assertEqual(6, curried(1, 2, 3))

  def test_can_be_partially_applied(self):
    curry3 = curryN(3)
    curried = curry3(source)
    self.assertEqual(6, curried(1)(2)(3))
    self.assertEqual(6, curried(1, 2)(3))
    self.assertEqual(6, curried(1)(2, 3))
    self.assertEqual(6, curried(1, 2, 3))

  # TODO: add placeholder tests

  def test_forwards_extra_arguments(self):
    def f(*arguments):
      return list(arguments)
    g = curryN(3, f)
    self.assertEqual([1, 2, 3], g(1, 2, 3))
    self.assertEqual([1, 2, 3, 4], g(1, 2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1, 2)(3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2, 3, 4))
    self.assertEqual([1, 2, 3, 4], g(1)(2)(3, 4))

if __name__ == '__main__':
  unittest.main()
