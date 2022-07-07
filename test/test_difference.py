import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/difference.js
"""

M = [1, 2, 3, 4]
M2 = [1, 2, 3, 4, 1, 2, 3, 4]
N = [3, 4, 5, 6]
N2 = [3, 3, 4, 4, 5, 5, 6, 6]
Z = [3, 4, 5, 6, 10]
Z2 = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8]


class TestDifference(unittest.TestCase):
  def test_finds_the_set_of_all_elements_in_the_first_list_not_contained_in_the_second(self):
    self.assertEqual([1, 2], R.difference(M, N))

  def test_does_not_allow_duplicates_in_the_output_even_if_the_input_lists_had_duplicates(self):
    self.assertEqual([1, 2], R.difference(M2, N2))

  def test_has_R_equals_semantics(self):
    self.assertEqual(1, len(R.difference([0.0], [-0.0])))
    self.assertEqual(0, len(R.difference([float('nan')], [float('nan')])))
    self.assertEqual(0, len(R.difference([Just([42])], [Just([42])])))

  def test_works_for_array_of_different_lengths(self):
    self.assertEqual([10], R.difference(Z, Z2))
    self.assertEqual([1, 2, 7, 8], R.difference(Z2, Z))

  def test_returns_an_empty_array_if_there_are_no_different_elements(self):
    self.assertEqual([], R.difference(M2, M))
    self.assertEqual([], R.difference(M, M2))
    self.assertEqual([], R.difference([], M2))


if __name__ == '__main__':
  unittest.main()
