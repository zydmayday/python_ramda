
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/join.js
"""


class TestJoin(unittest.TestCase):
  def test_concatenates_a_list_elements_to_a_string_with_an_separator_string_between_elements(self):
    arr = [1,2,3,4]
    self.assertEqual('1~2~3~4', R.join('~', arr))


if __name__ == '__main__':
  unittest.main()
