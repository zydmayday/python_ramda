
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/has.js
"""

dictFred = {'name': 'Fred', 'age': 23}
dictAnon = {'age': 99}


class Fred:
  def __init__(self):
    self.name = 'Fred'
    self.age = 23


class Anon:
  def __init__(self):
    self.age = 99


fred = Fred()
anon = Anon()


class TestHasForDict(unittest.TestCase):
  def test_returns_true_if_the_specified_property_is_present(self):
    self.assertEqual(True, R.has('name', dictFred))

  def test_returns_false_if_the_specified_property_is_absent(self):
    self.assertEqual(False, R.has('name', dictAnon))


class TestHasForObject(unittest.TestCase):
  def test_returns_true_if_the_specified_property_is_present(self):
    self.assertEqual(True, R.has('name', fred))

  def test_returns_false_if_the_specified_property_is_absent(self):
    self.assertEqual(False, R.has('name', anon))


class TestHasForOthers(unittest.TestCase):
  def test_does_not_check_static(self):
    class Person:
      static_var = 'static'
      def __init__(self):
        self.name = 'bob'
    bob = Person()

    self.assertEqual(True, R.has('name', bob))
    self.assertEqual(False, R.has('static_var', bob))

  def test_returns_false_for_non_objects(self):
    self.assertEqual(False, R.has('a', None))
    self.assertEqual(False, R.has('a', True))
    self.assertEqual(False, R.has('a', False))
    self.assertEqual(False, R.has('a', ''))

  def test_currying(self):
    self.assertEqual(True, R.has('a')({'a': {'b': 1}}))


if __name__ == '__main__':
  unittest.main()
