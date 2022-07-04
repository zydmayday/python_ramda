import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/indexOf.js
"""

input = [1, 2, 3, 4, 5]


class TestIndexOf(unittest.TestCase):
  def test_returns_a_number_indicating_an_object_position_in_a_list(self):
    arr = [0, 10, 20, 30]
    self.assertEqual(3, R.indexOf(30, arr))

  def test_returns_minus_one_if_the_object_is_not_in_the_list(self):
    arr = [0, 10, 20, 30]
    self.assertEqual(-1, R.indexOf(40, arr))

  def test_returns_the_index_of_the_first_item(self):
    self.assertEqual(0, R.indexOf(1, input))

  def test_returns_the_index_of_the_last_item(self):
    self.assertEqual(4, R.indexOf(5, input))

  def test_finds_1(self):
    self.assertEqual(0, R.indexOf(1, [1, 2, 3]))

  def test_does_not_consider_str_1_equal_to_1(self):
    self.assertEqual(-1, R.indexOf('1', [1, 2, 3]))

  def test_returns_minus_1_for_an_empty_array(self):
    self.assertEqual(-1, R.indexOf('x', []))

  def test_has_R_equals_semantics(self):
    self.assertEqual(1, len(R.difference([0.0], [-0.0])))
    self.assertEqual(0, R.indexOf(float('nan'), [float('nan')]))
    self.assertEqual(0, R.indexOf(Just([42]), [Just([42])]))

  def test_dispatches_to_indexOf_method(self):
    class Empty:
      def indexOf(self, *ignore):
        """
        indexOf method signature should be the same with List
        """
        return -1

    class List:
      def __init__(self, head, tail):
        self.head = head
        self.tail = tail

      def indexOf(self, x):
        idx = self.tail.indexOf(x)
        if self.head == x:
          return 0
        elif idx >= 0:
          return 1 + idx
        else:
          return -1

    arr = List('b',
               List('a',
                    List('n',
                         List('a',
                              List('n',
                                   List('a',
                                        Empty()
                                        )
                                   )
                              )
                         )
                    )
               )

    self.assertEqual(1, R.indexOf('a', 'banana'))
    self.assertEqual(-1, R.indexOf('x', 'banana'))
    self.assertEqual(1, R.indexOf('a', arr))
    self.assertEqual(-1, R.indexOf('x', arr))

  def test_finds_function_compared_by_identity(self):
    def f(): return None
    def g(): return None
    arr = [g, f, g, f]
    self.assertEqual(1, R.indexOf(f, arr))

  def test_does_not_find_function_compared_by_identity(self):
    def f(): return None
    def g(): return None
    def h(): return None
    arr = [g, f]
    self.assertEqual(-1, R.indexOf(h, arr))


if __name__ == '__main__':
  unittest.main()
