import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/append.js
"""


class TestAppend(unittest.TestCase):
  def test_adds_the_element_to_the_end_of_the_list(self):
    self.assertEqual(['x', 'y', 'z'], R.append('z', ['x', 'y']))
    self.assertEqual(['x', 'y', ['a', 'z']], R.append(['a', 'z'], ['x', 'y']))

  def test_works_on_empty_list(self):
    self.assertEqual([1], R.append(1, []))


if __name__ == '__main__':
  unittest.main()
