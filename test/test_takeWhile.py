
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/takeWhile.js
"""


class TestTakeWhile(unittest.TestCase):
  def test_continues_taking_elements_while_the_function_reports_true(self):
    self.assertEqual([1, 3], R.takeWhile(lambda x: x != 5, [1, 3, 5, 7, 9]))

  def test_starts_at_the_right_arg_and_acknowledges_undefined(self):
    self.assertEqual([], R.takeWhile(lambda: False, []))
    self.assertEqual([1, 3], R.takeWhile(lambda x: x is not None, [1, 3, None, 5, 7]))

  def test_can_operate_on_strings(self):
    self.assertEqual('Ram', R.takeWhile(lambda x: x != 'd', 'Ramda'))

  def test_can_act_as_a_transducer(self):
    def isNotFour(x): return x != 4
    input = [1, 2, 3, 4, 3, 2, 1]
    expected = [1, 2, 3]
    self.assertEqual(expected, R.into([], R.takeWhile(isNotFour), input))
    # TODO: transducer


if __name__ == '__main__':
  unittest.main()
