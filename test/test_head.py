import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/head.js
"""


class TestHead(unittest.TestCase):
  def test_returns_the_first_element_of_an_ordered_collection(self):
    self.assertEqual(1, R.head([1, 2, 3]))
    self.assertEqual(2, R.head([2, 3]))
    self.assertEqual(3, R.head([3]))
    self.assertEqual(None, R.head([]))

    self.assertEqual('a', R.head('abc'))
    self.assertEqual('b', R.head('bc'))
    self.assertEqual('c', R.head('c'))
    self.assertEqual('', R.head(''))

  def test_throws_if_applied_to_None(self):
    with self.assertRaises(TypeError):
      R.head(None)

if __name__ == '__main__':
  unittest.main()
