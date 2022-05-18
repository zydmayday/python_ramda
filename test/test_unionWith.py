
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/unionWith.js
"""

Ro = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
So = [{'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}]


def eqA(r, s):
  return r['a'] == s['a']


class TestUnionWith(unittest.TestCase):
  def test_combines_two_lists_into_the_set_of_all_their_elements_based_on_the_passed_in_quiality_predicate(self):
    self.assertEqual([{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}], R.unionWith(eqA, Ro, So))


if __name__ == '__main__':
  unittest.main()
