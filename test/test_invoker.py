
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/invoker.js
"""


concat2 = R.invoker(2, 'concat')


class Concater:
  def __init__(self, xs):
    self.xs = xs

  def concat(self, a, b):
    return self.xs + [a] + [b]


class TestInvoker(unittest.TestCase):
  def test_calls_the_method_on_the_object(self):
    self.assertEqual([1, 2, 3, 4], concat2(3, 4, Concater([1, 2])))

  def test_raises_a_descriptive_TypeError_if_method_does_not_exist(self):
    with self.assertRaises(TypeError):
      self.assertEqual([1, 2, 3, 4], concat2(3, 4, [1, 2]))

  def test_curries_the_method_call(self):
    self.assertEqual([1, 2, 3, 4], concat2(3)(4)(Concater([1, 2])))
    self.assertEqual([1, 2, 3, 4], concat2(3, 4)(Concater([1, 2])))
    self.assertEqual([1, 2, 3, 4], concat2(3)(4, Concater([1, 2])))


if __name__ == '__main__':
  unittest.main()
