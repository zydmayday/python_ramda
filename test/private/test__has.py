import unittest

from ramda.private._has import _has


class Test_has(unittest.TestCase):
  def test_array(self):
    self.assertEqual(False, _has([], 0))
    self.assertEqual(True, _has([1, 2, 3], 0))
    self.assertEqual(True, _has([1, 2, 3], 1))
    self.assertEqual(True, _has([1, 2, 3], 2))
    self.assertEqual(False, _has([1, 2, 3], 3))

  def test_dict(self):
    self.assertEqual(False, _has({}, 'a'))
    self.assertEqual(True, _has({'a': False, 'b': {'c': 1}}, 'a'))
    self.assertEqual(False, _has({'a': False, 'b': {'c': 1}}, 'c'))  # do not support nested dict
    self.assertEqual(True, _has({'a': False, 'b': {'c': 1}}, 'get'))  # do not check method

  def test_object(self):
    class Parent:
      c = 'parent static'

      def __init__(self):
        self.d = 'parent instance'

      def foo(self):
        return 'parent method'

    class Obj(Parent):
      a = 'static'

      def __init__(self, b):
        super().__init__()
        self.b = b

      def bar(self):
        return 'obj method'

    obj = Obj('b')

    self.assertEqual(True, _has(obj, 'a'))
    self.assertEqual(True, _has(obj, 'b'))
    self.assertEqual(True, _has(obj, 'c'))
    self.assertEqual(True, _has(obj, 'd'))
    self.assertEqual(True, _has(obj, 'foo'))
    self.assertEqual(True, _has(obj, 'bar'))

  def test_if_key_is_none(self):
    self.assertEqual(True, _has({None: False}, None))
    self.assertEqual(False, _has({'None': True}, None))


if __name__ == '__main__':
  unittest.main()
