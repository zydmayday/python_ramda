import unittest

import pamda as R

"""
https://github.com/ramda/ramda/blob/master/test/prop.js
"""

fred = {'name': 'Fred', 'age': 23}


class TestProp(unittest.TestCase):
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
    # TODO: implement path
    pass

  def test_shows_the_same_behaviour_as_path_for_a_None_property(self):
    # TODO: implement path
    pass

  def test_shows_the_same_behaviour_as_path_for_a_valid_property_and_object(self):
    # TODO: implement path
    pass

  def test_shows_the_same_behaviour_as_path_for_a_None_object(self):
    # TODO: implement path
    pass

  def test_returns_that_value_associated_to_a_property_given_valid_one(self):
    # TODO: implement path
    pass

  # TODO: add any(string, anthing, object) related tests

if __name__ == '__main__':
  unittest.main()
