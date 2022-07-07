import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/uniq.js
"""


class TestUniq(unittest.TestCase):
  def test_returns_a_set_from_any_array(self):
    self.assertEqual([1, 2, 3], R.uniq([1, 2, 3, 1, 2, 3, 1, 2, 3]))

  def test_keeps_elements_from_the_left(self):
    self.assertEqual([1, 2, 3, 4], R.uniq([1, 2, 3, 4, 1]))

  def test_returns_an_empty_array_for_an_empty_array(self):
    self.assertEqual([], R.uniq([]))

  def test_has_R_equals_semantics(self):
    self.assertEqual(1, len(R.uniq([-0.0, -0.0])))
    self.assertEqual(2, len(R.uniq([0.0, -0.0])))
    self.assertEqual(1, len(R.uniq([float('nan'), float('nan')])))
    # self.assertEqual(1, len(R.uniq([[1], [1]]))) # python only support hashable obj
    self.assertEqual(1, len(R.uniq([Just([42]), Just([42])])))

  def test_handles_None_elements(self):
    self.assertEqual([None], R.uniq([None, None, None]))

  def test_uses_reference_equality_for_functions(self):
    self.assertEqual(2, len(R.uniq([R.add, R.identity, R.add, R.identity, R.add, R.identity])))


if __name__ == '__main__':
  unittest.main()
