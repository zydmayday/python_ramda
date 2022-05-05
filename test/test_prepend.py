import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/prepend.js
"""


class TestPrepend(unittest.TestCase):
  def test_adds_the_element_to_the_beginning_of_the_list(self):
    self.assertEqual(['x', 'y', 'z'], R.prepend('x', ['y', 'z']))
    self.assertEqual([['a', 'z'], 'x', 'y'], R.prepend(['a', 'z'], ['x', 'y']))

  def test_works_on_empty_list(self):
    self.assertEqual([1], R.prepend(1, []))


if __name__ == '__main__':
  unittest.main()
