import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/empty.js
"""


class TestEmpty(unittest.TestCase):
  def test_dispatches_to_empty_method(self):
    class Nothing:
      def empty(self):
        return Nothing()

    class Just:
      def empty(self):
        return Nothing()
    self.assertTrue(isinstance(R.empty(Nothing()), Nothing))
    self.assertTrue(isinstance(R.empty(Just()), Nothing))

  def test_returns_empty_dict_given_dict(self):
    self.assertEqual({}, R.empty({'x': 1, 'y': 2}))

  def test_returns_empty_array_given_array(self):
    self.assertEqual([], R.empty([1, 2, 3]))

  def test_returns_empty_string_given_string(self):
    self.assertEqual('', R.empty('abc'))

  def test_returns_empty_set_given_set(self):
    self.assertEqual(set(), R.empty(set([1, 2, 3])))

  def test_returns_empty_None_given_None(self):
    self.assertEqual(None, R.empty(None))

  def test_returns_origin_object(self):
    class Obj:
      def __init__(self, value):
        self.value = value
    o = Obj(42)
    self.assertTrue(isinstance(R.empty(o), Obj))
    self.assertEqual(42, R.empty(o).value)


if __name__ == '__main__':
  unittest.main()
