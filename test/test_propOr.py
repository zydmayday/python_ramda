
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/propOr.js
"""

fred = {'name': 'Fred', 'age': 23}
anon = {'age': 99}

nm = R.propOr('Unknown', 'name')

class TestPropOrForDict(unittest.TestCase):
  def test_returns_a_function_that_fetches_the_appropriate_property(self):
    self.assertEqual('Fred', nm(fred))

  def test_returns_the_default_value_when_the_property_does_not_exist(self):
    self.assertEqual('Unknown', nm(anon))

  def test_returns_the_default_value_when_the_object_is_None(self):
    self.assertEqual('Unknown', nm(None))

  def test_uses_the_default_when_supplied_an_object_with_a_None_value(self):
    self.assertEqual('foo', R.propOr('foo', 'x', {'x': None}))

class Fred:
  def __init__(self):
    self.name = 'Fred'
    self.age = 23
fredObj = Fred()

class Anon:
  def __init__(self):
    self.age = 99
anonObj = Anon()

class TestPropOrForObject(unittest.TestCase):
  def test_returns_a_function_that_fetches_the_appropriate_property(self):
    self.assertEqual('Fred', nm(fredObj))

  def test_returns_the_default_value_when_the_property_does_not_exist(self):
    self.assertEqual('Unknown', nm(anonObj))

  def test_returns_the_default_value_when_the_object_is_None(self):
    self.assertEqual('Unknown', nm(None))

  def test_uses_the_default_when_supplied_an_object_with_a_None_value(self):
    class NoneObj:
      def __init__(self):
        self.x = None
    self.assertEqual('foo', R.propOr('foo', 'x', NoneObj()))

class TestPropOtherCases(unittest.TestCase):
  def test_handles_number_as_property(self):
    deities = ['Cthulhu', 'Dagon', 'Yog-Sothoth']
    self.assertEqual('Cthulhu', R.propOr('Unknown', 0, deities))
    self.assertEqual('Dagon', R.propOr('Unknown', 1, deities))
    self.assertEqual('Yog-Sothoth', R.propOr('Unknown', 2, deities))
    self.assertEqual('Yog-Sothoth', R.propOr('Unknown', -1, deities))
    self.assertEqual('Unknown', R.propOr('Unknown', 3, deities))

  def test_shows_the_same_behaviours_as_pathOr_for_a_nonexistent_property(self):
    # TODO: implement pathOr
    pass

if __name__ == '__main__':
  unittest.main()
