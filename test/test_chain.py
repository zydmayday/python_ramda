
import unittest

import ramda as R
from ramda.private._isTransformer import _isTransformer

from .helpers.Id import Id
from .helpers.listXf import listXf

"""
https://github.com/ramda/ramda/blob/master/test/chain.js
"""

intoArray = R.into([])
def add1(x): return [x + 1]
def dec(x): return [x - 1]
def times2(x): return [x * 2]


class TestChain(unittest.TestCase):
  def test_maps_a_function_over_a_nested_list_and_returns_the_shallow_flattened_result(self):
    self.assertEqual([2, 4, 6, 2, 0, 20, -6, 10, 14], R.chain(times2, [1, 2, 3, 1, 0, 10, -3, 5, 7]))
    self.assertEqual([2, 4, 6], R.chain(times2, [1, 2, 3]))

  def test_does_not_flatten_recursively(self):
    def f(xs):
      if len(xs) == 0:
        return []
      return [xs[0]]

    self.assertEqual([1, [2], 3], R.chain(f, [[1], [[2], 100], [], [3, [4]]]))

  def test_maps_a_function_into_a_shallow_flat_result(self):
    self.assertEqual([2, 4, 6, 8], intoArray(R.chain(times2), [1, 2, 3, 4]))

  def test_XFlatCat_if_input_is_not_arrayLike(self):
    self.assertEqual([2, 4, 6, 8], intoArray(R.chain(R.multiply(2)), [1, 2, 3, 4]))

  def test_interprets_r_as_a_monad(self):
    def h(r): return r * 2
    def f(a): return lambda r: r + a
    bound = R.chain(f, h)
    #  (>>=) :: (r -> a) -> (a -> r -> b) -> (r -> b)
    #  h >>= f = \w -> f (h w) w
    self.assertEqual((10 * 2) + 10, bound(10))
    self.assertEqual([1, 2, 3, 1], R.chain(R.append, R.head)([1, 2, 3]))

  def test_dispatches_to_objects_that_implement_chain(self):
    class Obj:
      def __init__(self, x):
        self.x = x

      def chain(self, f):
        return f(self.x)

    obj = Obj(100)
    self.assertEqual([101], R.chain(add1, obj))

  def test_dispatches_to_transformer_objects(self):
    self.assertEqual(True, _isTransformer(R.chain(add1, listXf)))

  def test_xFlatCat_if_input_not_arrayLike(self):
    add1ListXf = R.chain(add1, listXf)

  def test_composes(self):
    mdouble = R.chain(times2)
    mdec = R.chain(dec)
    self.assertEqual([19, 39, 59], mdec(mdouble([10, 20, 30])))

  def test_can_compose_transducer_style(self):
    mdouble = R.chain(times2)
    mdec = R.chain(dec)
    xcomp = R.compose(mdec, mdouble)
    self.assertEqual([18, 38, 58], intoArray(xcomp, [10, 20, 30]))

  def test_fantasy_land(self):
    id = R.chain(add1, Id(10))
    self.assertEqual([11], id)

  def test_forcedReduced(self):
    def reducedStep(acc, x):
      if x > 4:
        return R.reduced(acc + x)
      return acc + x
    reducedListXf = {
        '@@transducer/init': lambda: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        '@@transducer/step': reducedStep,
        '@@transducer/result': lambda x: x
    }
    times2ReducedListXf = R.chain(times2, reducedListXf)
    self.assertEqual((1 + 2 + 3) * 2, R.reduce(times2ReducedListXf, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    self.assertEqual((1 + 2) * 2, R.reduce(times2ReducedListXf, 0, [1, 2]))


if __name__ == '__main__':
  unittest.main()
