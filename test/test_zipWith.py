
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/zipWith.js
"""

a = [1, 2, 3]
b = [100, 200, 300]
c = [10, 20, 30, 40, 50, 60]
def s(a, b): return f'{a} cow {b}'


class TestZipWith(unittest.TestCase):
  def test_returns_an_array_created_by_applying_its_passed_in_function_pair_wise_on_its_passed_in_arrays(self):
    self.assertEqual([101, 202, 303], R.zipWith(R.add, a, b))
    self.assertEqual([100, 400, 900], R.zipWith(R.multiply, a, b))
    self.assertEqual(['1 cow 100', '2 cow 200', '3 cow 300'], R.zipWith(s, a, b))

  def test_returns_an_array_whose_length_is_equal_to_the_shorter_of_its_input_arrays(self):
    self.assertEqual(len(a), len(R.zipWith(R.add, a, c)))


if __name__ == '__main__':
  unittest.main()
