
import unittest

import ramda as R

from .helpers.listXf import listXf

"""
https://github.com/ramda/ramda/blob/master/test/findIndex.js
"""

obj1 = {'x': 100}
obj2 = {'x': 200}
a = [11, 10, 9, 'cow', obj1, 8, 7, 100, 200, 300, obj2, 4, 3, 2, 1, 0]
def even(x): return x % 2 == 0 if isinstance(x, int) else False
def gt100(x): return x > 100 if isinstance(x, int) else False
def isStr(x): return isinstance(x, str)
def xGt100(o): return o['x'] > 100 if isinstance(o, dict) and isinstance(o['x'], int) else False


class TestFindIndex(unittest.TestCase):
  def test_returns_the_index_of_the_first_element_that_satisfies_the_predicate(self):
    self.assertEqual(1, R.findIndex(even, a))
    self.assertEqual(8, R.findIndex(gt100, a))
    self.assertEqual(3, R.findIndex(isStr, a))
    self.assertEqual(10, R.findIndex(xGt100, a))

  def test_return_minus_one_when_no_element_satisfies_the_predicate(self):
    self.assertEqual(-1, R.findIndex(even, ['zing']))
    self.assertEqual(-1, R.findIndex(even, []))

  def test_dispatches_to_transformer_objects(self):
    res = R.findIndex(R.identity, listXf)
    self.assertEqual(R.identity, res.f)
    self.assertEqual(False, res.found)
    self.assertEqual(-1, res.idx)
    self.assertEqual(listXf, res.xf)

  def test_can_act_as_a_transducer(self):
    self.assertEqual([1], R.into([], R.findIndex(even), a))
    # TODO: transducer tests


if __name__ == '__main__':
  unittest.main()
