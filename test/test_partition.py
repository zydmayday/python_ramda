
import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/partition.js
"""


def pred(x): return x % 2


class TestPartition(unittest.TestCase):
  def test_splits_a_list_into_two_lists_according_to_a_predicate(self):
    self.assertEqual([[], []], R.partition(pred, []))
    self.assertEqual([[], [0, 2, 4, 6]], R.partition(pred, [0, 2, 4, 6]))
    self.assertEqual([[1, 3, 5, 7], []], R.partition(pred, [1, 3, 5, 7]))
    self.assertEqual([[1, 3], [0, 2]], R.partition(pred, [0, 1, 2, 3]))

  def test_works_with_dict(self):
    self.assertEqual([{}, {}], R.partition(pred, {}))
    self.assertEqual([{}, {'a': 0, 'b': 2, 'c': 4, 'd': 6}], R.partition(pred, {'a': 0, 'b': 2, 'c': 4, 'd': 6}))
    self.assertEqual([{'a': 1, 'b': 3, 'c': 5, 'd': 7}, {}], R.partition(pred, {'a': 1, 'b': 3, 'c': 5, 'd': 7}))
    self.assertEqual([{'b': 1, 'd': 3}, {'a': 0, 'c': 2}], R.partition(pred, {'a': 0, 'b': 1, 'c': 2, 'd': 3}))

  def test_works_with_object(self):
    class Empty:
      def __eq__(self, other):
        return isinstance(other, Empty)

      def equals(self, other):
        return isinstance(other, Empty)

    class Obj:
      def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

      def isEmpty(self):
        return not hasattr(self, 'a') and not hasattr(self, 'b') and not hasattr(self, 'c') and not hasattr(self, 'd')

      def __eq__(self, another):
        return self.a == another.a and self.b == another.b and self.c == another.c and self.d == another.d

    self.assertEqual([Empty(), Empty()], R.partition(pred, Empty()))

    res = R.partition(pred, Obj(0, 2, 4, 6))
    self.assertTrue(res[0].isEmpty())
    self.assertEqual(Obj(0, 2, 4, 6), res[1])

    res = R.partition(pred, Obj(1, 3, 5, 7))
    self.assertTrue(res[1].isEmpty())
    self.assertEqual(Obj(1, 3, 5, 7), res[0])

    res = R.partition(pred, Obj(0, 1, 2, 3))
    self.assertEqual(1, res[0].b)
    self.assertEqual(3, res[0].d)
    self.assertEqual(0, res[1].a)
    self.assertEqual(2, res[1].c)

  def test_works_with_other_filterables(self):
    just = Just([])
    res = R.partition(R.isEmpty, just)
    self.assertEqual(just, res[0])
    self.assertTrue(res[1].isNothing)

    just = Just([1])
    res = R.partition(R.isEmpty, just)
    self.assertTrue(res[0].isNothing)
    self.assertEqual(just, res[1])

    # TODO: complement


if __name__ == '__main__':
  unittest.main()
