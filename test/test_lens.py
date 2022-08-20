
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/lens.js
"""

alice = {
    'name': 'Alice Jones',
    'address': ['22 Walnut St', 'San Francisco', 'CA'],
    'pets': {'dog': 'joker', 'cat': 'batman'}
}

nameLens = R.lens(R.prop('name'), R.assoc('name'))
addressLens = R.lensProp('address')
headLens = R.lensIndex(0)
dogLens = R.lensPath(['pets', 'dog'])


class TestLens(unittest.TestCase):
  def test_may_be_applie_to_a_lens_created_by_lensPath(self):
    self.assertEqual('joker', R.view(dogLens, alice))

  def test_may_be_applied_to_a_lens_created_by_lensProp(self):
    self.assertEqual('Alice Jones', R.view(nameLens, alice))

    self.assertEqual({
        'name': 'ALICE JONES',
        'address': ['22 Walnut St', 'San Francisco', 'CA'],
        'pets': {'dog': 'joker', 'cat': 'batman'}
    }, R.over(nameLens, R.toUpper, alice))

    self.assertEqual({
        'name': 'Alice Smith',
        'address': ['22 Walnut St', 'San Francisco', 'CA'],
        'pets': {'dog': 'joker', 'cat': 'batman'}
    }, R.set(nameLens, 'Alice Smith', alice))

  def test_may_be_applied_to_a_lens_created_by_lensIndex(self):
    self.assertEqual('22 Walnut St', R.view(headLens, alice['address']))

    self.assertEqual(['22 WALNUT ST', 'San Francisco', 'CA'], R.over(headLens, R.toUpper, alice['address']))

    self.assertEqual(['52 Crane Ave', 'San Francisco', 'CA'], R.set(headLens, '52 Crane Ave', alice['address']))

  def test_may_be_applied_to_composed_lenses(self):
    streetLens = R.compose(addressLens, headLens)
    dogLens = R.compose(R.lensProp('pets'), R.lensProp('dog'))

    self.assertEqual(R.view(dogLens, alice), R.view(R.lensPath(['pets', 'dog']), alice))

    self.assertEqual('22 Walnut St', R.view(streetLens, alice))

    self.assertEqual({
        'name': 'Alice Jones',
        'address': ['22 WALNUT ST', 'San Francisco', 'CA'],
        'pets': {'dog': 'joker', 'cat': 'batman'}
    }, R.over(streetLens, R.toUpper, alice))

    self.assertEqual({
        'name': 'Alice Jones',
        'address': ['52 Crane Ave', 'San Francisco', 'CA'],
        'pets': {'dog': 'joker', 'cat': 'batman'}
    }, R.set(streetLens, '52 Crane Ave', alice))


if __name__ == '__main__':
  unittest.main()
