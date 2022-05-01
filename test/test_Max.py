
import datetime
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/max.js
"""


class TestMax(unittest.TestCase):
  def test_returns_the_larger_of_its_two_arguments(self):
    self.assertEqual(7, R.Max(-7, 7))
    self.assertEqual(7, R.Max(7, -7))

  def test_works_for_any_orderable_type(self):
    d1 = datetime.date(2001, 1, 1)
    d2 = datetime.date(2002, 2, 2)
    self.assertEqual(d2, R.Max(d1, d2))
    self.assertEqual(d2, R.Max(d2, d1))

    self.assertEqual('b', R.Max('a', 'b'))
    self.assertEqual('b', R.Max('b', 'a'))

  def test_returns_the_second_argument_if_both_arguments_are_equal(self):
    self.assertEqual(7, R.Max(7, 7))
    self.assertEqual(None, R.Max(None, None))

  def test_returns_the_alphabetically_later_type_if_neigher_argument_is_greater_than_the_other(self):
    self.assertEqual('a', R.Max('a', 7))
    self.assertEqual(None, R.Max('A', None))

  def test_returns_the_alphabetically_later_string_coersion_if_no_argument_or_type_is_greater_than_the_other(self):
    obj1 = {'a': 1}
    obj2 = {'a': 1}
    self.assertEqual(obj2, R.Max(obj1, obj2))
    self.assertEqual(obj1, R.Max(obj1, None))

  def test_returns_the_first_argument_if_no_other_comparison_attemps_produce_a_result(self):
    obj1 = {'a': 1}
    self.assertEqual(obj1, R.Max(obj1, obj1))
    self.assertTrue(R.equals(float('nan'), R.Max(float('nan'), float('nan'))))


if __name__ == '__main__':
  unittest.main()
