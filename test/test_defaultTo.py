
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/defaultTo.js
"""

defaultTo42 = R.defaultTo(42)

class TestDefaultTo(unittest.TestCase):
  def test_returns_the_default_value_if_input_is_None(self):
    self.assertEqual(42, defaultTo42(None))

  def test_returns_the_input_value_if_it_is_not_None(self):
    self.assertEqual('a real value', defaultTo42('a real value'))

  def test_returns_the_input_value_even_if_it_is_considered_falsy(self):
    self.assertEqual('', defaultTo42(''))
    self.assertEqual(0, defaultTo42(0))
    self.assertEqual(False, defaultTo42(False))
    self.assertEqual([], defaultTo42([]))

  def test_can_be_called_with_both_arguments_directly(self):
    self.assertEqual(42, R.defaultTo(42, None))
    self.assertEqual('a real value', R.defaultTo(42, 'a real value'))

if __name__ == '__main__':
  unittest.main()
