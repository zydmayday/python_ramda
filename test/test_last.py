
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/last.js
"""


class TestLast(unittest.TestCase):
  def test_returns_the_last_element_of_an_ordered_collection(self):
    self.assertEqual(3, R.last([1, 2, 3]))
    self.assertEqual(2, R.last([1, 2]))
    self.assertEqual(1, R.last([1]))
    self.assertEqual(None, R.last([]))

    self.assertEqual('c', R.last('abc'))
    self.assertEqual('b', R.last('ab'))
    self.assertEqual('a', R.last('a'))
    self.assertEqual('', R.last(''))

  def test_throws_if_applied_to_None(self):
    with self.assertRaises(TypeError):
      R.last(None)


if __name__ == '__main__':
  unittest.main()
