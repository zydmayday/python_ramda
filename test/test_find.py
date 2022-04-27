import unittest

import ramda as R
from ramda.private._has import _has

from .helpers.listXf import listXf

"""
https://github.com/ramda/ramda/blob/master/test/find.js
"""

obj1 = {'x': 100}
obj2 = {'x': 200}
a = [11, 10, 9, 'cow', obj1, 8, 7, 100, 200, 300, obj2, 4, 3, 2, 1, 0]
def even(x): return x % 2 == 0 if isinstance(x, int) else False
def gt100(x): return x > 100 if isinstance(x, int) else False
def isStr(x): return isinstance(x, str)
def xGt100(o): return o.get('x') > 100 if _has(o, 'get') else False


class TestFind(unittest.TestCase):
  def test_returns_the_first_elemenet_that_satisfies_the_predicate(self):
    self.assertEqual(10, R.find(even, a))
    self.assertEqual(200, R.find(gt100, a))
    self.assertEqual('cow', R.find(isStr, a))
    self.assertEqual(obj2, R.find(xGt100, a))

  def test_returns_None_when_no_element_statisfies_the_predicate(self):
    self.assertEqual(None, R.find(even, ['zing']))

  def test_returns_None_when_given_an_empty_list(self):
    self.assertEqual(None, R.find(even, []))

  def test_dispatches_to_transformer_objects(self):
    res = R.find(R.identity, listXf)
    self.assertEqual(res.f, R.identity)
    self.assertEqual(res.found, False)
    self.assertEqual(res.xf, listXf)

  def test_can_act_as_a_transducer(self):
    self.assertEqual([10], R.into([], R.find(even), a))
    # TODO: R.transduce


if __name__ == '__main__':
  unittest.main()
