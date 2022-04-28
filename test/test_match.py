
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/match.js
"""

re = r'[A-Z]\d\d\-[a-zA-Z]+'
matching = 'B17-afn'
notMatching = 'B1-afn'


class TestMatch(unittest.TestCase):
  def test_determines_whether_a_string_matches_a_regex(self):
    self.assertEqual(1, len(R.match(re, matching)))
    self.assertEqual(0, len(R.match(re, notMatching)))

  def test_defaults_to_a_different_empty_array_each_time(self):
    first = R.match(re, notMatching)
    second = R.match(re, notMatching)
    self.assertIsNot(first, second)

  def test_throws_on_null_input(self):
    with self.assertRaises(TypeError):
      R.match(re, None)

if __name__ == '__main__':
  unittest.main()
