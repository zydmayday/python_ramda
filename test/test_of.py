
import unittest

import ramda as R

from .helpers.Maybe import Just, Maybe

"""
https://github.com/ramda/ramda/blob/master/test/of.js
"""


class TestOf(unittest.TestCase):
  def test_returns_its_argument_as_an_array(self):
    self.assertEqual([100], R.of(list, 100))
    self.assertEqual([[100]], R.of(list, [100]))
    self.assertEqual([None], R.of(list, None))
    self.assertEqual([[]], R.of(list, []))

  def test_dispatches_to_an_available_of_method(self):
    class MaybeWithOf(Maybe):
      def of(x):
        return Just(x)

    just = R.of(MaybeWithOf, 100)
    self.assertTrue(R.equals(just, Just(100)))

  def test_dispatches_to_an_available_fantasy_land_of_method(self):
    class MaybeWithOf(Maybe):
      def get(self, name, default=None):
        if name == 'fantasy-land/of':
          return lambda x: Just(x)

    just = R.of(MaybeWithOf, 100)
    self.assertTrue(R.equals(just, Just(100)))


if __name__ == '__main__':
  unittest.main()
