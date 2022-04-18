import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/concat.js
"""


class Z1:
  x = 'z1'

  def concat(self, that):
    return self.x + ' ' + that.x


class Z2:
  x = 'z2'


z1 = Z1()
z2 = Z2()


class TestConcat(unittest.TestCase):
  def test_adds_combines_the_elements_of_two_lists(self):
    self.assertEqual(['a', 'b', 'c', 'd'], R.concat(['a', 'b'], ['c', 'd']))
    self.assertEqual(['c', 'd'], R.concat([], ['c', 'd']))

  def test_works_with_strings(self):
    self.assertEqual('foobar', R.concat('foo', 'bar'))
    self.assertEqual('x', R.concat('', 'x'))
    self.assertEqual('x', R.concat('x', ''))
    self.assertEqual('', R.concat('', ''))

  def test_delegates_to_non_strings_object_with_a_concat_method_as_second_param(self):
    self.assertEqual('z1 z2', R.concat(z1, z2))

  def test_throws_if_attemping_to_combine_an_array_with_a_non_array(self):
    with self.assertRaises(Exception):
      R.concat([1], 2)

  def test_throws_if_not_an_array_or_object_with_a_concat_method(self):
    with self.assertRaises(Exception):
      R.concat(z2, z1)

if __name__ == '__main__':
  unittest.main()
