import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/uniqBy.js
"""


class TestUniqBy(unittest.TestCase):
  def test_returns_a_set_from_any_array_based_on_predicate(self):
    self.assertEqual([-2, -1, 0], R.uniqBy(abs, [-2, -1, 0, 1, 2]))

  def test_keeps_elements_from_the_left(self):
    self.assertEqual([-1, 2, 4, 3], R.uniqBy(abs, [-1, 2, 4, 3, 1, 3]))

  def test_returns_an_empty_array_for_an_empty_array(self):
    self.assertEqual([], R.uniqBy(R.identity, []))

  def test_has_R_equals_semantics(self):
    self.assertEqual(2, len(R.uniqBy(R.identity, [0.0, -0.0])))
    self.assertEqual(1, len(R.uniqBy(R.identity, [float('nan'), float('nan')])))
    self.assertEqual(1, len(R.uniqBy(R.identity, [Just([1, 2, 3]), Just([1, 2, 3])])))

  def test_can_act_as_a_transducer(self):
    input = [-1, -5, 2, 10, 1, 2]
    expected = [-1, -5, 2, 10]
    self.assertEqual(expected, R.into([], R.uniqBy(abs), input))
    # TODO: R.transduce

if __name__ == '__main__':
  unittest.main()
