
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/values.js
"""

obj = {
    'a': 100,
    'b': [1, 2, 3],
    'c': {
        'x': 200,
        'y': 300
    },
    'd': 'D',
    'e': None
}


class C:
  def __init__(self, a, b):
    self.a = 100
    self.b = 200


cobj = C(100, 200)


class TestValues(unittest.TestCase):
  def test_returns_an_array_of_the_given_object_values(self):
    vs = R.values(obj)
    ts = [100, [1, 2, 3], {'x': 200, 'y': 300}, 'D', None]
    self.assertEqual(len(vs), len(ts))
    self.assertEqual(vs[0], ts[0])
    self.assertEqual(vs[1], ts[1])
    self.assertEqual(vs[2], ts[2])
    self.assertEqual(vs[3], ts[3])
    self.assertEqual(vs[4], ts[4])

  def test_works_on_objects(self):
    self.assertEqual([100, 200], R.values(cobj))

  def test_returns_an_empty_object_for_primitives(self):
    self.assertEqual([], R.values(None))
    self.assertEqual([], R.values(55))
    self.assertEqual([], R.values('foo'))
    self.assertEqual([], R.values(True))
    self.assertEqual([], R.values(False))
    self.assertEqual([], R.values([]))
    self.assertEqual([], R.values({}))


if __name__ == '__main__':
  unittest.main()
