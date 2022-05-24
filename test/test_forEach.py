
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/forEach.js
"""

arr = [{'x': 1, 'y': 2}, {'x': 100, 'y': 200}, {'x': 300, 'y': 400}, {'x': 234, 'y': 345}]


class TestForEach(unittest.TestCase):
  def test_performes_the_passed_in_function_on_each_element_of_the_list(self):
    sideEffect = {}

    def fn(elem):
      nonlocal sideEffect
      sideEffect[elem['x']] = elem['y']
    R.forEach(fn, arr)
    self.assertEqual(sideEffect, {1: 2, 100: 200, 300: 400, 234: 345})

  def test_returns_the_original_list(self):
    s = ''

    def fn(obj):
      nonlocal s
      s += str(obj['x'])
    self.assertEqual(arr, R.forEach(fn, arr))
    self.assertEqual(s, '1100300234')

  def test_handles_empty_list(self):
    self.assertEqual([], R.forEach(lambda x: x * x, []))

  def test_dispatches_to_forEach_method(self):
    dispatched = False

    def fn():
      return

    class DummyList:
      def forEach(this, callback):
        nonlocal dispatched
        dispatched = True
        self.assertEqual(fn, callback)

    R.forEach(fn, DummyList())
    self.assertEqual(True, dispatched)


if __name__ == '__main__':
  unittest.main()
