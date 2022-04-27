import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/filter.js
"""


def even(x): return x % 2 == 0 if isinstance(x, int) else False


class FilterObject:
  def filter(self, f):
    return f('called f.filter')


class Obj:
  def fn(self):
    return 'called fn'


class TestFilter(unittest.TestCase):
  def test_reduces_an_array_to_those_matching_a_filter(self):
    self.assertEqual([2, 4], R.filter(even, [1, 2, 3, 4, 5]))

  def test_returns_an_empty_array_if_no_element_matches(self):
    self.assertEqual([], R.filter(lambda x: x > 100, [1, 9, 99]))

  def test_returnsreduces_an_empty_array_if_asked_to_filter_an_empty_array(self):
    self.assertEqual([], R.filter(lambda x: x > 100, []))

  def test_filter_dict(self):
    def positive(x): return x > 0
    self.assertEqual({}, R.filter(positive, {}))
    self.assertEqual({}, R.filter(positive, {'x': 0, 'y': 0, 'z': 0}))
    self.assertEqual({'x': 1}, R.filter(positive, {'x': 1, 'y': 0, 'z': 0}))
    self.assertEqual({'x': 1, 'y': 2}, R.filter(positive, {'x': 1, 'y': 2, 'z': 0}))
    self.assertEqual({'x': 1, 'y': 2, 'z': 3}, R.filter(positive, {'x': 1, 'y': 2, 'z': 3}))

  def test_filter_objects(self):
    def positive(x): return x > 0
    o1 = Obj()
    o1.x = 0
    o1.y = 0
    o1.z = 0
    o1_expected = Obj()
    self.assertEqual(o1_expected.__dict__, R.filter(positive, o1).__dict__)

    o2 = Obj()
    o2.x = 1
    o2.y = 0
    o2.z = 0
    o2_expected = Obj()
    o2_expected.x = 1
    self.assertEqual(o2_expected.__dict__, R.filter(positive, o2).__dict__)

    o3 = Obj()
    o3.x = 1
    o3.y = 2
    o3.z = 0
    o3_expected = Obj()
    o3_expected.x = 1
    o3_expected.y = 2
    self.assertEqual(o3_expected.__dict__, R.filter(positive, o3).__dict__)

    o4 = Obj()
    o4.x = 1
    o4.y = 2
    o4.z = 3
    o4_expected = Obj()
    o4_expected.x = 1
    o4_expected.y = 2
    o4_expected.z = 3
    self.assertEqual(o4_expected.__dict__, R.filter(positive, o4).__dict__)

  def test_filter_objects_keep_functions(self):
    o = Obj()
    o_filtered = R.filter(lambda x: x > 0, o)
    self.assertEqual('called fn', o_filtered.fn())

  def test_dispatches_to_passedin_nonArray_object_with_a_filter_method(self):
    f = FilterObject()
    self.assertEqual('called f.filter', R.filter(lambda s: s, f))

  def test_correctly_uses_fantasy_land_implementation(self):
    m1 = Just(-1)
    m2 = R.filter(lambda x: x > 0, m1)
    self.assertEqual(True, m2.isNothing)

  def test_can_act_as_a_transducer(self):
    input = [1, 2, 3, 4]
    expected = [2, 4]
    self.assertEqual(expected, R.into([], R.filter(even), input))
    # TODO: R.transduce


if __name__ == '__main__':
  unittest.main()
