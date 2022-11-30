import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/pickBy.js
"""

obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


class TestPickBy(unittest.TestCase):
  def test_create_a_copy_of_the_object(self):
    self.assertEqual(obj, R.pickBy(R.always(True), obj))

  def test_when_returning_truth_keeps_the_key(self):
    self.assertEqual(obj, R.pickBy(R.T, obj))
    self.assertEqual(obj, R.pickBy(R.always({'a': 1}), obj))
    self.assertEqual(obj, R.pickBy(R.always(1), obj))

  def test_when_returning_falsy_do_not_keep_the_key(self):
    self.assertEqual({}, R.pickBy(R.F, obj))
    self.assertEqual({}, R.pickBy(R.always({}), obj))
    self.assertEqual({}, R.pickBy(R.always(0), obj))
    self.assertEqual({}, R.pickBy(R.always(None), obj))

  def test_is_called_with_val_key_obj(self):
    def pred(val, key, _obj):
      self.assertEqual(obj, _obj)
      return key == 'd' and val == 4
    self.assertEqual({'d': 4}, R.pickBy(pred, obj))

  def test_first_method_has_2_param(self):
    def pred(val, key):
      return key == 'd' and val == 4
    self.assertEqual({'d': 4}, R.pickBy(pred, obj))


if __name__ == '__main__':
  unittest.main()
