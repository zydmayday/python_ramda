
import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/union.js
"""

M = [1, 2, 3, 4]
N = [3, 4, 5, 6]


class TestUnion(unittest.TestCase):
  def test_combines_two_lists_into_the_set_of_all_their_elements(self):
    self.assertEqual([1, 2, 3, 4, 5, 6], R.union(M, N))

  def test_has_R_equals_semantics(self):
    self.assertEqual(2, len(R.union([0.0], [-0.0])))
    self.assertEqual(2, len(R.union([-0.0], [0.0])))
    self.assertEqual(1, len(R.union([float('nan')], [float('nan')])))
    self.assertEqual(1, len(R.union([Just([42])], [Just([42])])))


if __name__ == '__main__':
  unittest.main()
