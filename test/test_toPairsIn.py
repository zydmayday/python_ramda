
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/toPairsIn.js
"""


class TestToPairsIn(unittest.TestCase):
  def test_converts_a_dict_into_an_array_of_two_element_key_value_arrays(self):
    self.assertEqual([['a', 1], ['b', 2], ['c', 3]], R.toPairsIn({'a': 1, 'b': 2, 'c': 3}))

  def test_converts_an_object_into_an_array_of_two_element_key_value_arrays(self):
    class A:
      a = 'you can see me'

      def __init__(self, b):
        self.b = b
    a = A('b')
    self.assertEqual([['a', 'you can see me'], ['b', 'b']], R.toPairsIn(a))

    class B(A):
      c = 'you can see me too'

      def __init__(self, b, d):
        super().__init__(b)
        self.d = d
    b = B('b', 'd')
    self.assertEqual([['c', 'you can see me too'], ['a', 'you can see me'], ['b', 'b'], ['d', 'd']], R.toPairsIn(b))

    class C(A):
      c = 'you can see me too'

      def __init__(self, d):
        self.d = d
    c = C('d')
    self.assertEqual([['c', 'you can see me too'], ['a', 'you can see me'], ['d', 'd']], R.toPairsIn(c))


if __name__ == '__main__':
  unittest.main()
