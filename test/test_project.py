
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/project.js
"""

kids = [
    {'name': 'Abby', 'age': 7, 'hair': 'blond'},
    {'name': 'Fred', 'age': 12, 'hair': 'brown'},
    {'name': 'Rusty', 'age': 10, 'hair': 'brown'},
    {'name': 'Alois', 'age': 15, 'disposition': 'surly'},
]


class TestProject(unittest.TestCase):
  def test_selects_the_chosen_properties_from_each_element_in_a_list(self):
    self.assertEqual([
        {'name': 'Abby', 'age': 7},
        {'name': 'Fred', 'age': 12},
        {'name': 'Rusty', 'age': 10},
        {'name': 'Alois', 'age': 15},
    ], R.project(['name', 'age'], kids))

  def test_has_a_None_property_on_the_output_tuple_for_any_input_tuple_that_does_not_have_the_property(self):
    self.assertEqual([
        {'name': 'Abby', 'hair': 'blond'},
        {'name': 'Fred', 'hair': 'brown'},
        {'name': 'Rusty', 'hair': 'brown'},
        {'name': 'Alois', 'hair': None},
    ], R.project(['name', 'hair'], kids))

  def test_works_with_objects(self):
    class Human:
      def getName(self):
        return self.name

    class Kid(Human):
      def __init__(self, name, age, hair):
        self.name = name
        self.age = age
        self.hair = hair

      def fn(self):
        return self.name

    class Kid2(Human):
      def __init__(self, name, age, disposition):
        self.name = name
        self.age = age
        self.disposition = disposition

      def fn(self):
        return self.name

    abby = Kid('Abby', 7, 'blond')
    fred = Kid('Fred', 12, 'brown')
    rusty = Kid('Rusty', 10, 'brown')
    alois = Kid2('Alois', 15, 'surly')
    actual = R.project(['name', 'hair'], [abby, fred, rusty, alois])

    self.assertEqual('Abby', actual[0].name)
    self.assertEqual('blond', actual[0].hair)
    self.assertEqual('Fred', actual[1].name)
    self.assertEqual('brown', actual[1].hair)
    self.assertEqual('Rusty', actual[2].name)
    self.assertEqual('brown', actual[2].hair)
    self.assertEqual('Alois', actual[3].name)
    self.assertEqual(None, actual[3].hair)

    self.assertEqual('Abby', actual[0].fn()) # remain methods
    self.assertEqual('Alois', actual[3].fn()) # remain methods
    self.assertEqual('Abby', actual[0].getName()) # remain inherited methods
    self.assertEqual('Abby', actual[0].getName()) # remain inherited methods

if __name__ == '__main__':
  unittest.main()
