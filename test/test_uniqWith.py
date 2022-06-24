
import unittest

import ramda as R

from .helpers.listXf import listXfPushData

"""
https://github.com/ramda/ramda/blob/master/test/uniqWith.js
"""

objs = [
    {'x': R.T, 'i': 0}, {'x': R.F, 'i': 1}, {'x': R.T, 'i': 2}, {'x': R.T, 'i': 3},
    {'x': R.F, 'i': 4}, {'x': R.F, 'i': 5}, {'x': R.T, 'i': 6}, {'x': R.F, 'i': 7},
]
objs2 = [
    {'x': R.T, 'i': 0}, {'x': R.F, 'i': 1}, {'x': R.T, 'i': 2}, {'x': R.T, 'i': 3},
    {'x': R.F, 'i': 0}, {'x': R.T, 'i': 1}, {'x': R.F, 'i': 2}, {'x': R.F, 'i': 3},
]


def eqI(x, accX):
  return x['i'] == accX['i']


class TestUniqWith(unittest.TestCase):
  def test_returns_a_set_from_any_array_based_on_predicate(self):
    self.assertEqual(objs, R.uniqWith(eqI, objs))
    self.assertEqual([{'x': R.T, 'i': 0}, {'x': R.F, 'i': 1}, {'x': R.T, 'i': 2}, {'x': R.T, 'i': 3}], R.uniqWith(eqI, objs2))

  def test_keeps_element_from_the_left(self):
    self.assertEqual([{'i': 1}, {'i': 2}, {'i': 3}, {'i': 4}], R.uniqWith(eqI, [{'i': 1}, {'i': 2}, {'i': 3}, {'i': 4}, {'i': 1}]))

  def test_returns_an_empty_array_for_an_empty_array(self):
    self.assertEqual([], R.uniqWith(eqI, []))

  def test_can_act_as_a_transducer(self):
    input = [1, '1', 2, 1]
    expected = [1, 2]
    # TODO: eqBy
    # TODO: transduce

  def test_uniqWith_xf(self):
    uniqWithXf = R.uniqWith(lambda x, y: x % 2 == y % 2, listXfPushData)
    res = R.reduce(uniqWithXf, [], [1, 2, 3, 4, 5])
    self.assertEqual([1, 2], res)


if __name__ == '__main__':
  unittest.main()
