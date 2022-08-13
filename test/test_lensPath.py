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

  def test_sets_the_value_of_the_object_property_specified(self):
    self.assertEqual({'a': [{'b': 1}, {'b': 2}], 'd': 0}, R.set(R.lensPath(['d']), 0, testDict))
    self.assertEqual({'a': [{'b': 0}, {'b': 2}], 'd': 3}, R.set(R.lensPath(['a', 0, 'b']), 0, testDict))
    self.assertEqual(0, R.set(R.lensPath([]), 0, testDict))

    # TODO: support object, refer assoc

  def test_adds_the_property_to_the_object_if_it_does_not_exist(self):
    self.assertEqual({'a': [{'b': 1}, {'b': 2}], 'd': 3, 'X': 0}, R.set(R.lensPath(['X']), 0, testDict))
    self.assertEqual({'a': [{'b': 1, 'X': 0}, {'b': 2}], 'd': 3}, R.set(R.lensPath(['a', 0, 'X']), 0, testDict))

    # TODO: support object, refer assoc

  def test_applies_function_to_the_value_of_the_specified_object_property(self):
    self.assertEqual({'a': [{'b': 1}, {'b': 2}], 'd': 4}, R.over(R.lensPath(['d']), R.inc, testDict))
    self.assertEqual({'a': [{'b': 1}, {'b': 3}], 'd': 3}, R.over(R.lensPath(['a', 1, 'b']), R.inc, testDict))
    self.assertEqual([['a', [{'b': 1}, {'b': 2}]], ['d', 3]], R.over(R.lensPath([]), R.toPairs, testDict))

    # TODO: support object, refer assoc

  def test_applies_function_to_None_and_adds_the_property_if_it_does_not_exists(self):
    self.assertEqual({'a': [{'b': 1}, {'b': 2}], 'd': 3, 'X': None}, R.over(R.lensPath(['X']), R.identity, testDict))
    self.assertEqual({'a': [{'b': 1, 'X': None}, {'b': 2}], 'd': 3}, R.over(R.lensPath(['a', 0, 'X']), R.identity, testDict))

    # TODO: support object, refer assoc

  def test_can_be_composed(self):
    composedLens = R.compose(R.lensPath(['a']), R.lensPath([1, 'b']))
    self.assertEqual(2, R.view(composedLens, testDict))
    self.assertEqual(2, R.view(composedLens, testObj))

  def test_set_s_get_s_equals_s(self):
    # set s (get s) == s
    self.assertEqual(testDict, R.set(R.lensPath(['d']), R.view(R.lensPath(['d']), testDict), testDict))
    self.assertEqual(testDict, R.set(R.lensPath(['a', 0, 'b']), R.view(R.lensPath(['a', 0, 'b']), testDict), testDict))

    # TODO: support object, refer assoc

  def test_get_set_s_v_equals_v(self):
    # get (set s v) == v
    self.assertEqual(0, R.view(R.lensPath(['d']), R.set(R.lensPath(['d']), 0, testDict)))
    self.assertEqual(0, R.view(R.lensPath(['a', 0, 'b']), R.set(R.lensPath(['a', 0, 'b']), 0, testDict)))

    # TODO: support object, refer assoc

  def test_get_set_set_s_v1_v2_equals_v2(self):
    # get (set (set s v1) v2) == v2
    p = ['d']
    q = ['a', 0, 'b']
    self.assertEqual(11, R.view(R.lensPath(p), R.set(R.lensPath(p), 11, R.set(R.lensPath(p), 10, testDict))))
    self.assertEqual(11, R.view(R.lensPath(q), R.set(R.lensPath(q), 11, R.set(R.lensPath(q), 10, testDict))))

    # TODO: support object, refer assoc


if __name__ == '__main__':
  unittest.main()
