import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/sort.js
"""


class TestSort(unittest.TestCase):
  def test_sorts_the_elements_of_a_list(self):
    self.assertEqual([1, 1, 2, 3, 5, 8], R.sort(lambda a, b: a - b, [3, 1, 8, 1, 2, 5]))

  def test_does_not_affect_the_list_passed_supplied(self):
    arr = [3, 1, 8, 1, 2, 5]
    self.assertEqual([1, 1, 2, 3, 5, 8], R.sort(lambda a, b: a - b, arr))
    self.assertEqual([3, 1, 8, 1, 2, 5], arr)


if __name__ == '__main__':
  unittest.main()
