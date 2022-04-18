import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/reverse.js
"""


class TestReverse(unittest.TestCase):
  def test_reverses_arrays(self):
    self.assertEqual([], R.reverse([]))
    self.assertEqual([1], R.reverse([1]))
    self.assertEqual([1, 2], R.reverse([2, 1]))
    self.assertEqual([1, 2, 3], R.reverse([3, 2, 1]))

  def test_reverses_twice_an_array_should_be_the_array_itself(self):
    self.assertEqual([1, 2, 3], R.reverse(R.reverse([1, 2, 3])))

  def test_reverses_strings(self):
    self.assertEqual('', R.reverse(''))
    self.assertEqual('1', R.reverse('1'))
    self.assertEqual('12', R.reverse('21'))
    self.assertEqual('123', R.reverse('321'))

  def test_reverses_twice_a_string_should_be_the_string_itself(self):
    self.assertEqual('123', R.reverse(R.reverse('123')))


if __name__ == '__main__':
  unittest.main()
