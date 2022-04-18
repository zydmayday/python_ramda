import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/differenceWith.js
"""

Ro = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
Ro2 = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}, {'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
So = [{'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}]
So2 = [{'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}, {'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}]
def eqA(r, s): return r['a'] == s['a']
def identical(a, b): return a == b


class TestDifferenceWith(unittest.TestCase):
  def test_combines_two_lists_into_the_set_of_all_their_elements_based_on_the_pased_in_equality_predicate(self):
    self.assertEqual([{'a': 1}, {'a': 2}], R.differenceWith(eqA, Ro, So))

  def test_does_not_allow_duplicates_in_the_output_even_if_the_input_lists_had_duplicates(self):
    self.assertEqual([{'a': 1}, {'a': 2}], R.differenceWith(eqA, Ro2, So2))

if __name__ == '__main__':
  unittest.main()
