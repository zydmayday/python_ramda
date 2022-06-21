
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/toPairs.js
"""


class TestToPairs(unittest.TestCase):
  def test_converts_a_dict_into_an_array_of_two_element_key_value_arrays(self):
    self.assertEqual([['a', 1], ['b', 2], ['c', 3]], R.toPairs({'a': 1, 'b': 2, 'c': 3}))

  def test_converts_an_object_into_an_array_of_two_element_key_value_arrays(self):
    class A:
      a = 1

      def __init__(self, b, c):
        self.b = b
        self.c = c
    a = A(2, 3)
    self.assertEqual([['b', 2], ['c', 3]], R.toPairs(a))

    class B(A):
      d = 4

      def __init__(self, b, c, e):
        super().__init__(b, c)
        self.e = e

    b = B(2, 3, 5)
    self.assertEqual([['b', 2], ['c', 3], ['e', 5]], R.toPairs(b))

    # without super()
    class C(A):
      d = 4

      def __init__(self, e):
        self.e = e

    c = C(5)
    self.assertEqual([['e', 5]], R.toPairs(c))


if __name__ == '__main__':
  unittest.main()
