
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/split.js
"""


class TestSplit(unittest.TestCase):
  def test_splits_a_string_into_an_array(self):
    self.assertEqual(['a', 'b', 'c', 'xyz', 'd'], R.split('.', 'a.b.c.xyz.d'))

  def test_the_split_string_can_be_arbitrary(self):
    self.assertEqual(['The C', ' in the H', ' s', ' on the m', ''], R.split('at', 'The Cat in the Hat sat on the mat'))

if __name__ == '__main__':
  unittest.main()
