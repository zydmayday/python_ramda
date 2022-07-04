
import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/propEq.js
"""

dict1 = {'name': 'Abby', 'age': 7, 'hair': 'blond'}
dict2 = {'name': 'Fred', 'age': 12, 'hair': 'brown'}


class TestPropEq(unittest.TestCase):
  def test_has_R_equals_semantics(self):
    self.assertEqual(False, R.propEq(0.0, 'value', {'value': -0.0}))
    self.assertEqual(False, R.propEq(-0.0, 'value', {'value': 0.0}))
    self.assertEqual(True, R.propEq(float('nan'), 'value', {'value': float('nan')}))
    self.assertEqual(True, R.propEq(Just([42]), 'value', {'value': Just([42])}))

  def test_returns_False_if_called_with_None(self):
    self.assertEqual(False, R.propEq('Abby', 'name', None))

class TestPropEqForDict(unittest.TestCase):
  def test_determines_whether_a_particular_property_matches_a_given_value_for_a_specific_object(self):
    self.assertEqual(True, R.propEq('Abby', 'name', dict1))
    self.assertEqual(True, R.propEq('brown', 'hair', dict2))
    self.assertEqual(False, R.propEq('blond', 'hair', dict2))

class TestPropEqForObject(unittest.TestCase):
  def test_determines_whether_a_particular_property_matches_a_given_value_for_a_specific_object(self):
    class Person:
      def __init__(self, name, age, hair):
        self.name = name
        self.age = age
        self.hair = hair
    abby = Person('Abby', 7, 'blond')
    fred = Person('Fred', 12, 'brown')
    self.assertEqual(True, R.propEq('Abby', 'name', abby))
    self.assertEqual(True, R.propEq('brown', 'hair', fred))
    self.assertEqual(False, R.propEq('blond', 'hair', fred))

class TestPropEqForList(unittest.TestCase):
  def test_handles_number_as_property(self):
    deities=['Cthulhu', 'Dagon', 'Yog-Sothoth']
    self.assertEqual(True, R.propEq('Cthulhu', 0, deities))
    self.assertEqual(True, R.propEq('Dagon', 1, deities))
    self.assertEqual(True, R.propEq('Yog-Sothoth', 2, deities))
    self.assertEqual(True, R.propEq('Yog-Sothoth', -1, deities))
    self.assertEqual(True, R.propEq(None, 3, deities))


if __name__ == '__main__':
  unittest.main()
