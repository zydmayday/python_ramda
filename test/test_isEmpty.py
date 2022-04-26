
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/isEmpty.js
"""


class TestIsEmpty(unittest.TestCase):
  def test_returns_False_for_None(self):
    self.assertEqual(False, R.isEmpty(None))

  def test_returns_True_for_empty_string(self):
    self.assertEqual(True, R.isEmpty(''))
    self.assertEqual(False, R.isEmpty(' '))

  def test_returns_True_for_empty_array(self):
    self.assertEqual(True, R.isEmpty([]))
    self.assertEqual(False, R.isEmpty([[]]))

  def test_returns_True_for_empty_dict(self):
    self.assertEqual(True, R.isEmpty({}))
    self.assertEqual(False, R.isEmpty({'x': 0}))

  def test_returns_True_for_empty_set(self):
    self.assertEqual(True, R.isEmpty(set()))
    self.assertEqual(False, R.isEmpty(set([1])))

  def test_object_is_not_empty(self):
    class Obj:
      pass
    self.assertEqual(False, R.isEmpty(Obj()))


if __name__ == '__main__':
  unittest.main()
