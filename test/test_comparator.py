import unittest
from functools import cmp_to_key

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/comparator.js
"""


class TestComparator(unittest.TestCase):
  def test_builds_a_comparator_function_for_sorting_out_of_a_simple_predicate_that_reports_whether_the_first_param_is_smaller(self):
    self.assertEqual([1, 1, 2, 3, 5, 8], sorted([3, 1, 8, 1, 2, 5], key=cmp_to_key(R.comparator(lambda a, b: a < b))))


if __name__ == '__main__':
  unittest.main()
