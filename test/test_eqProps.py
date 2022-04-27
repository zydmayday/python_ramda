import unittest

import ramda as R

from .helpers.Maybe import Just

"""
https://github.com/ramda/ramda/blob/master/test/eqProps.js
"""

a = []
b = a


class TestEqProps(unittest.TestCase):
  def test_reports_whether_two_dicts_have_the_same_value_for_a_given_property(self):
    self.assertEqual(True, R.eqProps('name', {'name': 'fred', 'age': 10}, {'name': 'fred', 'age': 12}))
    self.assertEqual(False, R.eqProps('name', {'name': 'fred', 'age': 10}, {'name': 'franny', 'age': 10}))

  def test_reports_whether_two_objects_have_the_same_value_for_a_given_property(self):
    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
    fred1 = Person('fred', 10)
    fred2 = Person('fred', 12)
    franny = Person('franny', 10)
    self.assertEqual(True, R.eqProps('name', fred1, fred2))
    self.assertEqual(False, R.eqProps('name', fred1, franny))

  def test_has_R_equals_semantics(self):
    self.assertEqual(True, R.eqProps('value', {'value': Just([42])}, {'value': Just([42])}))


if __name__ == '__main__':
  unittest.main()
