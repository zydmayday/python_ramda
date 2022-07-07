import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/intersection.js
"""

M = [1, 2, 3, 4]
M2 = [1, 2, 3, 4, 1, 2, 3, 4]
N = [3, 4, 5, 6]
N2 = [3, 3, 4, 4, 5, 5, 6, 6]


class TestIntersection(unittest.TestCase):
  def test_combines_two_lists_into_the_set_of_common_elements(self):
    self.assertEqual([3, 4], R.intersection(M, N))

  def test_does_not_allow_duplicates_in_the_output_even_if_the_input_lists_had_duplicates(self):
    self.assertEqual([3, 4], R.intersection(M2, N2))

  def test_does_not_allow_duplicates_in_the_output_even_if_the_first_lists_is_bigger_and_has_duplicates(self):
    self.assertEqual([3, 4], R.intersection(M2, N))

  def test_does_not_allow_duplicates_in_the_output_even_if_the_second_lists_is_bigger_and_has_duplicates(self):
    self.assertEqual([3, 4], R.intersection(M, N2))

  def test_has_R_equals_semantics(self):
    self.assertEqual(0, len(R.intersection([0.0], [-0.0])))
    self.assertEqual(0, len(R.intersection([-0.0], [0.0])))
    self.assertEqual(1, len(R.intersection([float('nan')], [float('nan')])))
    self.assertEqual(1, len(R.intersection([Just([42])], [Just([42])])))


if __name__ == '__main__':
  unittest.main()
