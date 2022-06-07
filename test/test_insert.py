
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/insert.js
"""

arr = ['a', 'b', 'c', 'd', 'e']


class TestInsert(unittest.TestCase):
  def test_inserts_an_element_into_the_given_list(self):
    self.assertEqual(['a', 'b', 'x', 'c', 'd', 'e'], R.insert(2, 'x', arr))

  def test_inserts_another_list_as_an_element(self):
    self.assertEqual(['a', 'b', ['s', 't'], 'c', 'd', 'e'], R.insert(2, ['s', 't'], arr))

  def test_appends_to_the_end_of_the_list_if_the_index_is_too_large(self):
    self.assertEqual(['a', 'b', 'c', 'd', 'e', 'z'], R.insert(8, 'z', arr))


if __name__ == '__main__':
  unittest.main()
