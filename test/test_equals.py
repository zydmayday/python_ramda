import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/equals.js
"""

a = []
b = a


class TestEquals(unittest.TestCase):
  def test_for_deep_equality_of_its_operands(self):
    self.assertEqual(True, R.equals(100, 100))
    self.assertEqual(False, R.equals(100, '100'))
    self.assertEqual(True, R.equals(a, b))

  def test_considers_equal_boolean_primitives_equal(self):
    self.assertEqual(True, R.equals(True, True))
    self.assertEqual(True, R.equals(False, False))
    self.assertEqual(False, R.equals(True, False))
    self.assertEqual(False, R.equals(False, True))

  def test_considers_equivalent_boolean_objects_equal(self):
    self.assertEqual(True, R.equals(bool(True), bool(True)))
    self.assertEqual(True, R.equals(bool(False), bool(False)))
    self.assertEqual(False, R.equals(bool(True), bool(False)))
    self.assertEqual(False, R.equals(bool(False), bool(True)))

  # NOTICE: python does not have bool object

  def test_bool_with_objects(self):
    class T:
      def __bool__(self):
        return True

    class F:
      def __bool__(self):
        return False
    t = T()
    f = F()
    self.assertEqual(True, R.equals(bool(t), True))
    self.assertEqual(False, R.equals(bool(t), False))
    self.assertEqual(True, R.equals(bool(f), False))
    self.assertEqual(False, R.equals(bool(f), True))

  def test_considers_equal_number_primitives_equal(self):
    self.assertEqual(True, R.equals(0, 0))
    self.assertEqual(False, R.equals(0, 1))
    self.assertEqual(False, R.equals(1, 0))

  def test_considers_equal_string_primitives_equal(self):
    self.assertEqual(True, R.equals('', ''))
    self.assertEqual(False, R.equals('', 'x'))
    self.assertEqual(False, R.equals('x', ''))
    self.assertEqual(True, R.equals('foo', 'foo'))
    self.assertEqual(False, R.equals('foo', 'bar'))
    self.assertEqual(False, R.equals('bar', 'foo'))

    # Test python style str
    self.assertEqual(True, R.equals('foo', "foo"))
    self.assertEqual(True, R.equals('foo', """foo"""))
    self.assertEqual(True, R.equals('foo', '''foo'''))
    self.assertEqual(True, R.equals("foo", """foo"""))
    self.assertEqual(True, R.equals("foo", '''foo'''))
    self.assertEqual(True, R.equals("""foo""", '''foo'''))
    self.assertEqual(True, R.equals('1', str(1)))
    self.assertEqual(True, R.equals("1", str(1)))
    self.assertEqual(True, R.equals('''1''', str(1)))
    self.assertEqual(True, R.equals("""1""", str(1)))

  def test_handle_dicts(self):
    self.assertEqual(True, R.equals({}, {}))
    self.assertEqual(True, R.equals({'a': 1, 'b': 2}, {'a': 1, 'b': 2}))
    self.assertEqual(True, R.equals({'a': 1, 'b': 2}, {'b': 2, 'a': 1}))
    self.assertEqual(False, R.equals({'a': 2, 'b': 2}, {'b': 2, 'a': 1}))
    self.assertEqual(False, R.equals({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'a': 1}))

  def test_considers_equivalent_arguments_objects_equal(self):
    a = (lambda *args: args)()
    b = (lambda *args: args)()
    c = (lambda *args: args)(1, 2, 3)
    d = (lambda *args: args)(1, 2, 3)

    self.assertEqual(True, R.equals(a, b))
    self.assertEqual(True, R.equals(b, a))
    self.assertEqual(True, R.equals(c, d))
    self.assertEqual(True, R.equals(d, c))
    self.assertEqual(False, R.equals(a, c))
    self.assertEqual(False, R.equals(c, a))

  def test_considers_equivalent_error_objects_equal(self):
    self.assertEqual(True, R.equals(ValueError('XXX'), ValueError('XXX')))
    self.assertEqual(False, R.equals(ValueError('XXX'), ValueError('YYY')))
    self.assertEqual(False, R.equals(IndexError('XXX'), ValueError('XXX')))
    self.assertEqual(False, R.equals(IndexError('XXX'), ValueError('YYY')))

  # regex is not built-in type in python, so we don't support it yet
  # TODO: support regex

  def test_handles_list(self):
    listA = [1, 2, 3]
    listB = [1, 3, 2]
    self.assertEqual(False, R.equals([], {}))
    self.assertEqual(False, R.equals(listA, listB))

  def test_handles_reacursieve_data_structures(self):
    c = {}
    c['v'] = c
    d = {}
    d['v'] = d
    e = []
    e.append(e)
    f = []
    f.append(f)
    nestA = {'a': [1, 2, {'c': 1}], 'b': 1}
    nestB = {'a': [1, 2, {'c': 1}], 'b': 1}
    nestC = {'a': [1, 2, {'c': 2}], 'b': 1}
    # Python can not compare such recursive data structure
    # self.assertEqual(True, R.equals(c, d))
    # self.assertEqual(True, R.equals(e, f))
    self.assertEqual(True, R.equals(nestA, nestB))
    self.assertEqual(False, R.equals(nestA, nestC))

    # date is not built-in type in python, so we don't support it yet
    # TODO: support date

  def test_compares_set_objects_by_value(self):
    self.assertEqual(True, R.equals(set(), set()))
    self.assertEqual(False, R.equals(set([]), set([1])))
    self.assertEqual(False, R.equals(set([]), set([1])))
    self.assertEqual(True, R.equals(set([1, 2]), set([2, 1])))
    # self.assertEqual(True, R.equals(set([1, set([2, set([3])])]), set(1, [set([2, set([3])])])))
    # self.assertEqual(True, R.equals(set([[1, 2, 3], [4, 5, 6]]), set([[4, 5, 6], [1, 2, 3]])))
    # self.assertEqual(True, R.equals(set([[1, 2, 3], [4, 5, 6]]), set([[4, 5, 6], [7, 8, 9]])))

  def test_compares_WeakMap_objects_by_identity(self):
    """
    ref: https://docs.python.org/3/library/weakref.html
    """
    class Dict(dict):
      pass
    d = Dict()
    self.assertEqual(True, R.equals(d, d))
    # TODO: catch up with weakref
    # TODO: WeakSet if need
    # self.assertEqual(False, R.equals(d, Dict()))

  def test_dispatches_to_equals_method_recursively(self):
    class Left:
      def __init__(self, x):
        self.value = x
      def equals(self, x):
        return isinstance(x, Left) and R.equals(self.value, x.value)

    class Right:
      def __init__(self, x):
        self.value = x
      def equals(self, x):
        return isinstance(x, Right) and R.equals(self.value, x.value)

    self.assertEqual(True, R.equals(Left([42]), Left([42])))
    self.assertEqual(False, R.equals(Left([42]), Left([43])))
    self.assertEqual(False, R.equals(Left(42), {'value': 42}))
    self.assertEqual(False, R.equals({'value': 42}, Left(42)))
    self.assertEqual(False, R.equals(Left(42), Right(42)))
    self.assertEqual(False, R.equals(Right(42), Left(42)))

    self.assertEqual(True, R.equals([Left(42)], [Left(42)]))
    self.assertEqual(False, R.equals([Left(42)], [Right(42)]))
    self.assertEqual(False, R.equals([Right(42)], [Left(42)]))
    self.assertEqual(True, R.equals([Right(42)], [Right(42)]))

  def test_is_commutative(self):
    class Point:
      def __init__(self, x, y):
        self.x = x
        self.y = y
      def equals(self, point):
        return isinstance(point, Point) and self.x == point.x and self.y == point.y

    class ColorPoint:
      def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
      def equals(self, point):
        return isinstance(point, ColorPoint) and self.x == point.x and self.y == point.y and self.color == point.color

    self.assertEqual(True, R.equals(Point(1, 2), Point(1, 2)))
    self.assertEqual(True, R.equals(ColorPoint(1, 2, 'red'), ColorPoint(1, 2, 'red')))
    self.assertEqual(False, R.equals(Point(1, 2), ColorPoint(1, 2, 'red')))
    self.assertEqual(False, R.equals(ColorPoint(1, 2, 'red'), Point(1, 2)))

  def test_nan(self):
    self.assertEqual(True, R.equals(float('nan'), float('nan')))

if __name__ == '__main__':
  unittest.main()
