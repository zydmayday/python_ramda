
import unittest

import ramda as R

from .helpers.listXf import listXf

"""
https://github.com/ramda/ramda/blob/master/test/map.js
"""


def times2(x): return x * 2
def add1(x): return x + 1
def dec(x): return x - 1


class A:
  def __init__(self):
    self.a = 1


class B(A):
  def __init__(self):
    super().__init__()
    self.b = 2


class C:
  def __init__(self, x):
    self.x = x

  def map(self, f):
    return f(self.x)


class TestMap(unittest.TestCase):
  def test_maps_simple_functions_over_array(self):
    self.assertEqual([2, 4, 6, 8], R.map(times2, [1, 2, 3, 4]))

  def test_maps_over_objects(self):
    a, b = A(), B()
    mappedA = R.map(dec, a)
    mappedB = R.map(dec, b)
    self.assertEqual(0, mappedA.a)
    self.assertEqual(0, mappedB.a)
    self.assertEqual(1, mappedB.b)

    # make sure not change original objects
    self.assertEqual(1, a.a)
    self.assertEqual(1, b.a)
    self.assertEqual(2, b.b)

  def test_maps_over_dicts(self):
    self.assertEqual({}, R.map(dec, {}))
    self.assertEqual({'x': 3, 'y': 4, 'z': 5}, R.map(dec, {'x': 4, 'y': 5, 'z': 6}))

  def test_interprets_as_a_functor(self):
    def f(a): return a - 1
    def g(b): return b * 2
    h = R.map(f, g)
    self.assertEqual((10 * 2) - 1, h(10))

  def test_dispatches_to_objects_that_implement_map(self):
    c = C(42)
    self.assertEqual(41, R.map(dec, c))

  def test_dispatches_to_transformer_objects(self):
    o = R.map(add1, listXf)
    self.assertEqual(add1, o.f)
    self.assertEqual(listXf, o.xf)

  def test_throws_an_Exception_on_None(self):
    with self.assertRaises(Exception):
      R.map(times2, None)

  def test_composes(self):
    mdouble = R.map(times2)
    mdec = R.map(dec)
    self.assertEqual([19, 39, 59], mdec(mdouble([10, 20, 30])))

  def test_can_compose_transducer_style(self):
    mdouble = R.map(times2)
    mdec = R.map(dec)
    xcomp = mdec(mdouble(listXf))
    self.assertEqual(dec, xcomp.f)
    self.assertEqual(listXf, xcomp.xf.xf)
    self.assertEqual(times2, xcomp.xf.f)

  def test_can_act_as_a_transducer(self):
    self.assertEqual([2, 4, 6, 8], R.into([], R.map(times2), [1, 2, 3, 4]))
    # TODO: R.transduce


if __name__ == '__main__':
  unittest.main()
