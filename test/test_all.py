import unittest

import ramda as R

from .helpers.listXf import listXf

"""
https://github.com/ramda/ramda/blob/master/test/all.js
"""


def even(n): return n % 2 == 0
def T(): return True
def isFalse(x): return x == False


intoArray = R.into([])


class TestAll(unittest.TestCase):
  def test_returns_true_if_all_elements_satisfy_the_predicate(self):
    self.assertEqual(True, R.all(even, [2, 4, 6, 8, 10, 12]))
    self.assertEqual(True, R.all(isFalse, [False, False, False]))

  def test_false_if_any_element_fails_to_satisfy_the_predicate(self):
    self.assertEqual(False, R.all(even, [2, 4, 6, 8, 9, 10]))

  def test_true_for_an_empty_list(self):
    self.assertEqual(True, R.all(T, []))

  def test_true_into_array_if_all_elements_satisfy_the_predicate(self):
    self.assertEqual([True], intoArray(R.all(even), [2, 4, 6, 8, 10, 12]))
    self.assertEqual([True], intoArray(R.all(isFalse), [False, False, False]))

  def test_false_into_array_if_any_element_failes_to_satisfy_the_predicate(self):
    self.assertEqual([False], intoArray(R.all(even), [2, 4, 6, 8, 9, 10]))

  def test_true_into_array_for_an_empty_list(self):
    self.assertEqual([True], intoArray(R.all(T), []))

  def test_works_with_more_complex_objects(self):
    xs = [{'x': 'abc'}, {'x': 'ade'}, {'x': 'fghiajk'}]
    def len3(o): return len(o.get('x')) == 3
    def hasA(o): return 'a' in o.get('x')
    self.assertEqual(False, R.all(len3, xs))
    self.assertEqual(True, R.all(hasA, xs))

  def test_dispatches_when_given_a_transformer_in_list_position(self):
    res = R.all(even, listXf)
    self.assertEqual(res.all, True)
    self.assertEqual(res.f, even)
    self.assertEqual(res.xf, listXf)

  def test_can_act_as_a_transducer(self):
    input = [2, 4, 6, 8, 9, 10]
    expected = [False]
    self.assertEqual(expected, R.into([], R.all(even), input))
    # TODO: R.transduce


if __name__ == '__main__':
  unittest.main()
