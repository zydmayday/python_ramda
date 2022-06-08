import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/prop.js
"""

fred = {'name': 'Fred', 'age': 23}


class TestPropForDict(unittest.TestCase):
  def test_returns_a_function_that_fetches_the_appropriate_property(self):
    nm = R.prop('name')
    self.assertEqual('Fred', nm(fred))

  def test_handles_number_as_property(self):
    deities = ['Cthulhu', 'Dagon', 'Yog-Sothoth']
    self.assertEqual('Cthulhu', R.prop(0, deities))
    self.assertEqual('Dagon', R.prop(1, deities))
    self.assertEqual('Yog-Sothoth', R.prop(2, deities))
    self.assertEqual('Yog-Sothoth', R.prop(-1, deities))

  def test_shows_the_same_behaviour_as_path_for_a_nonexistent_property(self):
    propResult = R.prop('incorrect', fred)
    pathResult = R.path(['incorrect'], fred)
    self.assertEqual(propResult, pathResult)

  def test_shows_the_same_behaviour_as_path_for_a_None_property(self):
    propResult = R.prop(None, fred)
    pathResult = R.path([None], fred)
    self.assertEqual(propResult, pathResult)

  def test_shows_the_same_behaviour_as_path_for_a_valid_property_and_object(self):
    propResult = R.prop('age', fred)
    pathResult = R.path(['age'], fred)
    self.assertEqual(propResult, pathResult)

  def test_shows_the_same_behaviour_as_path_for_a_None_object(self):
    propResult = R.prop('age', None)
    pathResult = R.path(['age'], None)
    self.assertEqual(propResult, pathResult)

class Fred:
  def __init__(self):
    self.name = 'Fred'
    self.age = 23
fredObj = Fred()
class TestPropForObject(unittest.TestCase):
  def test_returns_a_function_that_fetches_the_appropriate_property(self):
    nm = R.prop('name')
    self.assertEqual('Fred', nm(fredObj))

  def test_shows_the_same_behaviour_as_path_for_a_nonexistent_property(self):
    propResult = R.prop('incorrect', fredObj)
    pathResult = R.path(['incorrect'], fredObj)
    self.assertEqual(propResult, pathResult)

  def test_shows_the_same_behaviour_as_path_for_a_None_property(self):
    propResult = R.prop(None, fredObj)
    pathResult = R.path([None], fredObj)
    self.assertEqual(propResult, pathResult)

  def test_shows_the_same_behaviour_as_path_for_a_valid_property_and_object(self):
    propResult = R.prop('age', fredObj)
    pathResult = R.path(['age'], fredObj)
    self.assertEqual(propResult, pathResult)

  def test_shows_the_same_behaviour_as_path_for_a_None_object(self):
    propResult = R.prop('age', None)
    pathResult = R.path(['age'], None)
    self.assertEqual(propResult, pathResult)

if __name__ == '__main__':
  unittest.main()
