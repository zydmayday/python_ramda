import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/lensPath.js
"""

testDict = {
    'a': [{
        'b': 1
    }, {
        'b': 2
    }],
    'd': 3
}


class A:
  def __init__(self, b):
    self.b = b


class Obj:
  def __init__(self, a, d):
    self.a = a
    self.d = d


testObj = Obj([A(1), A(2)], 3)


class TestLensPath(unittest.TestCase):
  def test_focuses_the_specified_object_property(self):
    self.assertEqual(3, R.view(R.lensPath(['d']), testDict))
    self.assertEqual(2, R.view(R.lensPath(['a', 1, 'b']), testDict))
    self.assertEqual(testDict, R.view(R.lensPath([]), testDict))

    self.assertEqual(3, R.view(R.lensPath(['d']), testObj))
    self.assertEqual(2, R.view(R.lensPath(['a', 1, 'b']), testObj))
    self.assertEqual(testObj, R.view(R.lensPath([]), testObj))

if __name__ == '__main__':
  unittest.main()
