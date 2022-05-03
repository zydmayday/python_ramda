
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/pick.js
"""

obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


class TestPick(unittest.TestCase):
  def test_copies_the_named_properties_of_an_object_to_the_new_object(self):
    self.assertEqual({'a': 1, 'c': 3, 'f': 6}, R.pick(['a', 'c', 'f'], obj))

  def test_ignores_properties_not_included(self):
    self.assertEqual({'a': 1, 'c': 3}, R.pick(['a', 'c', 'g'], obj))

  def test_work_with_objects(self):
    class Obj:
      def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    o = Obj(1, 2, 3, 4, 5, 6)
    omittedObj = R.pick(['a', 'c', 'f'], o)
    self.assertEqual(1, omittedObj.a)
    self.assertEqual(False, hasattr(omittedObj, 'b'))
    self.assertEqual(3, omittedObj.c)
    self.assertEqual(False, hasattr(omittedObj, 'd'))
    self.assertEqual(False, hasattr(omittedObj, 'e'))
    self.assertEqual(6, omittedObj.f)

    # not changed the original object
    self.assertEqual(1, o.a)
    self.assertEqual(2, o.b)
    self.assertEqual(3, o.c)
    self.assertEqual(4, o.d)
    self.assertEqual(5, o.e)
    self.assertEqual(6, o.f)


if __name__ == '__main__':
  unittest.main()
