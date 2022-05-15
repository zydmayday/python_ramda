
import unittest
from itertools import count

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/take.js
"""


class TestTake(unittest.TestCase):
  def test_takes_only_the_first_n_elements_from_a_list(self):
    self.assertEqual(['a', 'b', 'c'], R.take(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))

  def test_returns_only_as_many_as_the_array_can_provide(self):
    self.assertEqual([1, 2], R.take(3, [1, 2]))
    self.assertEqual([], R.take(3, []))

  def test_returns_an_equivalent_list_if_n_is_negative(self):
    self.assertEqual([1, 2, 3], R.take(-1, [1, 2, 3]))

  def test_never_returns_the_input_array(self):
    xs = [1, 2, 3]
    self.assertIsNot(xs, R.take(3, xs))
    self.assertIsNot(xs, R.take(-1, xs))

  def test_can_operate_on_strings(self):
    self.assertEqual('Ram', R.take(3, 'Ramda'))
    self.assertEqual('Ra', R.take(2, 'Ramda'))
    self.assertEqual('R', R.take(1, 'Ramda'))
    self.assertEqual('', R.take(0, 'Ramda'))

  def test_handles_zero_correctly(self):
    self.assertEqual([], R.into([], R.take(0), [1, 2, 3]))

  def test_steps_correct_number_of_times(self):
    count = 0

    def spy(_):
      nonlocal count
      count += 1

    R.into([], R.compose(R.map(spy), R.take(2)), [1, 2, 3])
    self.assertEqual(2, count)

  def test_transducer_called_for_every_member_of_list_if_n_is_negative(self):
    count = 0

    def spy(_):
      nonlocal count
      count += 1

    R.into([], R.compose(R.map(spy), R.take(-1)), [1, 2, 3])
    self.assertEqual(3, count)


if __name__ == '__main__':
  unittest.main()
