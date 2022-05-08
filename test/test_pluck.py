
import unittest

import ramda as R
from ramda.private._isFunction import _isFunction

"""
https://github.com/ramda/ramda/blob/master/test/pluck.js
"""

people = [
    {'name': 'Fred', 'age': 23},
    {'name': 'Wilma', 'age': 21},
    {'name': 'Pebbles', 'age': 2},
]


class TestPluck(unittest.TestCase):
  def test_returns_a_function_that_maps_the_appropriate_property_over_an_array(self):
    nm = R.pluck('name')
    self.assertTrue(_isFunction(nm))
    self.assertEqual(['Fred', 'Wilma', 'Pebbles'], nm(people))

  def test_work_with_a_pure_dict(self):
    obj = {'a': {'val': 3}, 'b': {'val': 5}}
    self.assertEqual({'a': 3, 'b': 5}, R.pluck('val', obj))

  def test_works_with_objects(self):
    nm = R.pluck('name')

    class People:
      def __init__(self, name, age):
        self.name = name
        self.age = age
    fred = People('Fred', 23)
    wilma = People('Wilma', 21)
    pebbles = People('Pebbles', 2)
    self.assertEqual(['Fred', 'Wilma', 'Pebbles'], nm([fred, wilma, pebbles]))

  def test_behaves_as_a_transducer_when_given_a_transducer_in_list_position(self):
    numbers = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
    # TODO: transduce


if __name__ == '__main__':
  unittest.main()
