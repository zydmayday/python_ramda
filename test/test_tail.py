import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/tail.js
"""


class TestTail(unittest.TestCase):
  def test_returns_the_tail_of_an_ordered_collection(self):
    self.assertEqual([2, 3], R.tail([1, 2, 3]))
    self.assertEqual([3], R.tail([2, 3]))
    self.assertEqual([], R.tail([3]))
    self.assertEqual([], R.tail([]))

    self.assertEqual('bc', R.tail('abc'))
    self.assertEqual('c', R.tail('bc'))
    self.assertEqual('', R.tail('c'))
    self.assertEqual('', R.tail(''))

  def test_exception_if_work_with_none(self):
    with self.assertRaises(TypeError):
      R.tail(None)


if __name__ == '__main__':
  unittest.main()
