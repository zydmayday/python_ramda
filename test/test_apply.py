
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/apply.js
"""


class TestApply(unittest.TestCase):
  def test_applies_function_to_argument_list(self):
    self.assertEqual(42, R.apply(max, [1, 2, 3, -99, 42, 6, 7]))

if __name__ == '__main__':
  unittest.main()
