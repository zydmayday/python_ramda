
import unittest

import ramda as R
from ramda.private._isFunction import _isFunction

"""
https://github.com/ramda/ramda/blob/master/test/hasIn.js
"""

dictFred = {'name': 'Fred', 'age': 23}
dictAnon = {'age': 99}


class Fred:
  def __init__(self, name, age):
    self.name = name
    self.age = age


class Anon:
  def __init__(self, age):
    self.age = age


fred = Fred('Fred', 23)
anon = Anon(99)


class TestHasInForDict(unittest.TestCase):
  def test_returns_a_function_that_checks_the_appropiate_property(self):
    nm = R.hasIn('name')
    self.assertEqual(True, _isFunction(nm))
    self.assertEqual(True, nm(dictFred))
    self.assertEqual(False, nm(dictAnon))


class TestHasInForObject(unittest.TestCase):
  def test_returns_a_function_that_checks_the_appropiate_property(self):
    nm = R.hasIn('name')
    self.assertEqual(True, _isFunction(nm))
    self.assertEqual(True, nm(fred))
    self.assertEqual(False, nm(anon))

  def test_checks_properties_from_parent(self):
    class Person:
      def __init__(self, name):
        self.name = name

    class Bob(Person):
      def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    bob = Bob('Bob', 23)
    self.assertEqual(True, R.hasIn('name', bob))


class TestHasInForOthers(unittest.TestCase):
  def test_works_properly_when_called_with_two_arguments(self):
    self.assertEqual(True, R.hasIn('name', fred))
    self.assertEqual(False, R.hasIn('name', anon))

  def test_returns_false_when_non_existent_object(self):
    self.assertEqual(False, R.hasIn('name', None))


if __name__ == '__main__':
  unittest.main()
