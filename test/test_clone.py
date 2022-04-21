import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/clone.js
"""


class TestCloneIntegersStringAndBooleans(unittest.TestCase):
  def test_clones_integers(self):
    self.assertEqual(-4, R.clone(-4))
    self.assertEqual(9007199254740991, R.clone(9007199254740991))

  def test_clones_floats(self):
    self.assertEqual(-4.5, R.clone(-4.5))
    self.assertEqual(0.0, R.clone(0.0))

  def test_clones_strings(self):
    self.assertEqual('ramda', R.clone('ramda'))

  def test_clones_booleans(self):
    self.assertEqual(True, R.clone(True))


class TestDeepCloneObjects(unittest.TestCase):
  def test_clones_object(self):
    class Obj:
      def __init__(self, x):
        self.value = x
    obj = Obj(42)
    clone = R.clone(obj)
    self.assertEqual(False, obj == clone)
    self.assertEqual(True, isinstance(clone, Obj))

  def test_clones_object_override_eq(self):
    class Obj:
      def __init__(self, x):
        self.value = x

      def __eq__(self, other):
        return self.value == other.value

      def get(self):
        return self.value

      def set(self, value):
        self.value = value

    obj = Obj(10)
    clone = R.clone(obj)
    self.assertEqual(True, obj == clone)

    self.assertEqual(10, obj.get())
    self.assertEqual(10, clone.get())

    obj.set(11)
    self.assertEqual(11, obj.get())
    self.assertEqual(10, clone.get())


class TestDeepCloneDicts(unittest.TestCase):
  def test_clones_shallow_dict(self):
    class Date:
      def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

      def setDate(self, day):
        self.day = day

      def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    obj = {'a': 1, 'b': 'ramda', 'c': True, 'd': Date(2013, 11, 25)}
    clone = R.clone(obj)
    obj['c'] = False
    obj['d'].setDate(31)
    self.assertEqual({'a': 1, 'b': 'ramda', 'c': True, 'd': Date(2013, 11, 25)}, clone)

  def test_clones_deep_dict(self):
    obj = {'a': {'b': {'c': 'ramda'}}}
    clone = R.clone(obj)
    obj['a']['b']['c'] = None
    self.assertEqual({'a': {'b': {'c': 'ramda'}}}, clone)

  def test_clones_dict_with_circular_references(self):
    x = {'c': None}
    y = {'a': x}
    z = {'b': y}
    x['c'] = z
    clone = R.clone(x)
    # self.assertEqual(x, clone) Python does not support this
    # RecursionError: maximum recursion depth exceeded in comparison


class TestDeepCloneArrays(unittest.TestCase):
  def test_clones_shallow_arrays(self):
    arr = [1, 2, 3]
    clone = R.clone(arr)
    arr.pop()
    self.assertEqual([1, 2, 3], clone)

  def test_clones_deep_arrays(self):
    arr = [1, [1, 2, 3], [[[5]]]]
    clone = R.clone(arr)
    self.assertEqual(arr, clone)
    self.assertEqual(arr[2], clone[2])
    self.assertEqual(arr[2][0], clone[2][0])

    self.assertEqual([1, [1, 2, 3], [[[5]]]], clone)


class TestDeepCloneFunctions(unittest.TestCase):
  def test_keep_reference_to_function(self):
    def fn(x): return x + x
    arr = [{'a': fn}]
    clone = R.clone(arr)
    self.assertEqual(20, clone[0]['a'](10))
    self.assertEqual(clone[0]['a'], arr[0]['a'])

  class TestBuildInTypes(unittest.TestCase):
    # TODO: regex and date is not built-in in Python
    # So we skip the test case for now
    pass


class TestCloneDeepNestedMixedObjects(unittest.TestCase):
  def test_clones_array_with_dicts(self):
    arr = [{'a': {'b': 1}}, [{'c': {'d': 1}}]]
    clone = R.clone(arr)
    arr[1][0] = None
    self.assertEqual([{'a': {'b': 1}}, [{'c': {'d': 1}}]], clone)

  def test_clones_array_with_arrays(self):
    arr = [[1], [[3]]]
    clone = R.clone(arr)
    arr[1][0] = None
    self.assertEqual([[1], [[3]]], clone)

  def test_clones_array_with_mutual_ref_dict(self):
    obj = {'a': 1}
    arr = [{'b': obj}, {'b': obj}]
    clone = R.clone(arr)
    self.assertEqual(arr[0]['b'], clone[1]['b'])
    self.assertEqual(clone[0]['b'], arr[1]['b'])
    self.assertEqual(clone[0]['b'], arr[0]['b'])
    self.assertEqual(clone[1]['b'], arr[1]['b'])

    self.assertEqual({'a': 1}, clone[0]['b'])
    self.assertEqual({'a': 1}, clone[1]['b'])

    obj['a'] = 2
    self.assertEqual({'a': 1}, clone[0]['b'])
    self.assertEqual({'a': 1}, clone[1]['b'])

class TestDeepCloneEdgeCases(unittest.TestCase):
  def test_None_and_empty_dict_and_arrays(self):
    self.assertEqual(None, R.clone(None))
    self.assertEqual({}, R.clone({}))
    self.assertEqual([], R.clone([]))

class TestUseAnArbitraryUserDefinedCloneMethod(unittest.TestCase):
  def test_dispatches_to_clone_method_if_present(self):
    class ArbitraryClone:
      def __init__(self, x):
        self.value = x
      def clone(self):
        return ArbitraryClone(self.value)

    obj = ArbitraryClone(42)
    ArbitraryCloneObj = R.clone(obj)
    self.assertEqual(42, ArbitraryCloneObj.value)
    self.assertEqual(True, isinstance(ArbitraryCloneObj, ArbitraryClone))


if __name__ == '__main__':
  unittest.main()
