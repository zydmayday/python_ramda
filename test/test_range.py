import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/range.js
"""


class TestRange(unittest.TestCase):
  def test_returns_list_of_numbers(self):
    self.assertEqual([0, 1, 2, 3, 4], R.range(0, 5))
    self.assertEqual([4, 5, 6], R.range(4, 7))

  def test_returns_the_empty_list_if_the_first_parameter_is_not_larger_than_the_second(self):
    self.assertEqual([], R.range(7, 3))
    self.assertEqual([], R.range(5, 5))

  def test_returns_an_empty_array_if_from_larger_than_to(self):
    result = R.range(10, 5)
    self.assertEqual([], result)
    result.append(5)
    self.assertEqual([], R.range(10, 5))

  def test_terminates_given_bad_input(self):
    with self.assertRaises(TypeError):
      R.range('a', 'z')


if __name__ == '__main__':
  unittest.main()
