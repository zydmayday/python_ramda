
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/repeat.js
"""


class TestRepeat(unittest.TestCase):
  def test_returns_a_lazy_list_of_identical_values(self):
    self.assertEqual([0, 0, 0, 0, 0], R.repeat(0, 5))

  def test_can_accept_any_value_including_None(self):
    self.assertEqual([None, None, None], R.repeat(None, 3))


if __name__ == '__main__':
  unittest.main()
