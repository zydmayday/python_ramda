
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/omit.js
"""

obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


class TestOmit(unittest.TestCase):
  def test_copies_an_dict_ommitting_the_listed_properties(self):
    self.assertEqual({'b': 2, 'd': 4, 'e': 5}, R.omit(['a', 'c', 'f'], obj))

  def test_copies_an_dict_ommitting_the_listed_properties_includes_not_present_keys_in_input(self):
    self.assertEqual({'b': 2, 'd': 4, 'e': 5, 'f': 6}, R.omit(['a', 'c', 'g'], obj))

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
    omittedObj = R.omit(['a', 'c', 'f'], o)
    self.assertEqual(False, hasattr(omittedObj, 'a'))
    self.assertEqual(2, omittedObj.b)
    self.assertEqual(False, hasattr(omittedObj, 'c'))
    self.assertEqual(4, omittedObj.d)
    self.assertEqual(5, omittedObj.e)
    self.assertEqual(False, hasattr(omittedObj, 'f'))

    # not changed the original object
    self.assertEqual(1, o.a)
    self.assertEqual(2, o.b)
    self.assertEqual(3, o.c)
    self.assertEqual(4, o.d)
    self.assertEqual(5, o.e)
    self.assertEqual(6, o.f)


if __name__ == '__main__':
  unittest.main()
