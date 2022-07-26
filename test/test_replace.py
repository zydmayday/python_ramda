
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/replace.js
"""


class TestReplace(unittest.TestCase):
  def test_replaces_substrings_of_the_input_string(self):
    self.assertEqual('one two three', R.replace('1', 'one', '1 two three'))

  def test_replaces_regex_matches_of_the_input_string(self):
    self.assertEqual('num num three', R.replace(r'\d+', 'num', '1 2 three'))

  def test_replaces_curry(self):
    self.assertEqual('num num three', R.replace(r'\d+')('num')('1 2 three'))


if __name__ == '__main__':
  unittest.main()
