
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/zip.js
"""


class TestZip(unittest.TestCase):
  def test_returns_an_array_of_tuples(self):
    a = [1, 2, 3]
    b = [100, 200, 300]
    self.assertEqual([[1, 100], [2, 200], [3, 300]], R.zip(a, b))

  def test_returns_a_list_as_long_as_the_shorter_of_the_lists_input(self):
    a = [1, 2, 3]
    b = [100, 200, 300, 400]
    c = [10, 20]
    self.assertEqual([[1, 100], [2, 200], [3, 300]], R.zip(a, b))
    self.assertEqual([[1, 10], [2, 20]], R.zip(a, c))

if __name__ == '__main__':
  unittest.main()
