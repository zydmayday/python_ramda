
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/is.js
"""


class TestIs(unittest.TestCase):
  def test_works_with_built_in_types(self):

    # Numeric types
    self.assertTrue(R.Is(int, 1))
    self.assertTrue(R.Is(float, 1.1))
    self.assertTrue(R.Is(complex, 1 + 1j))

    self.assertFalse(R.Is(int, 1.1))
    self.assertFalse(R.Is(float, 1))
    self.assertFalse(R.Is(complex, 1))

    # Sequence types
    self.assertTrue(R.Is(list, []))
    self.assertTrue(R.Is(tuple, ()))

    self.assertTrue(R.Is(list, [1, 2, 3]))
    self.assertTrue(R.Is(tuple, (1, 2, 3)))

    self.assertFalse(R.Is(tuple, [1, 2, 3]))
    self.assertFalse(R.Is(list, (1, 2, 3)))

    # Text Sequence types
    self.assertTrue(R.Is(str, ""))
    self.assertTrue(R.Is(str, 'abc'))
    self.assertTrue(R.Is(str, '''abc'''))
    self.assertTrue(R.Is(str, u'abc'))
    self.assertTrue(R.Is(str, f'abc'))
    self.assertTrue(R.Is(str, r'abc'))

    self.assertFalse(R.Is(str, b'abc'))

    # Binary Sequence types
    self.assertTrue(R.Is(bytes, b""))
    self.assertTrue(R.Is(bytearray, bytearray(b"")))
    self.assertTrue(R.Is(memoryview, memoryview(b"")))

    # Set types
    self.assertTrue(R.Is(set, set()))
    self.assertTrue(R.Is(frozenset, frozenset()))

    self.assertTrue(R.Is(set, set([1, 2, 3])))
    self.assertTrue(R.Is(frozenset, frozenset([1, 2, 3])))

    self.assertFalse(R.Is(frozenset, set([1, 2, 3])))
    self.assertFalse(R.Is(set, frozenset([1, 2, 3])))

    # Mapping types
    self.assertTrue(R.Is(dict, {}))
    self.assertTrue(R.Is(dict, {'a': 1, 'b': 2}))
    self.assertTrue(R.Is(dict, dict()))
    self.assertTrue(R.Is(dict, dict(a=1, b=2)))

    # Union types
    # From python 3.10+
    # u = int | str
    # self.assertTrue(R.Is(u, 1))
    # self.assertTrue(R.Is(u, "1"))

    # None type
    self.assertTrue(R.Is(None, None))

    # Boolean types
    self.assertTrue(R.Is(bool, True))
    self.assertTrue(R.Is(bool, False))

  def test_works_with_objects(self):
    class A:
      pass

    class B(A):
      pass

    class C(B):
      pass

    a = A()
    b = B()
    c = C()

    self.assertTrue(R.Is(A, a))
    self.assertFalse(R.Is(B, a))
    self.assertFalse(R.Is(C, a))

    self.assertTrue(R.Is(A, b))
    self.assertTrue(R.Is(B, b))
    self.assertFalse(R.Is(C, b))

    self.assertTrue(R.Is(A, c))
    self.assertTrue(R.Is(B, c))
    self.assertTrue(R.Is(C, c))

  def test_does_not_coerce(self):
    self.assertFalse(R.Is(int, "1"))
    self.assertFalse(R.Is(float, "1"))


if __name__ == '__main__':
  unittest.main()
