
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/toUpper.js
"""


class TestToUpper(unittest.TestCase):
  def test_returns_the_upper_case_equivalent_of_the_input_string(self):
    self.assertEqual('ABC', R.toUpper('abc'))


if __name__ == '__main__':
  unittest.main()
