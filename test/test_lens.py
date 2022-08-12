
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
# addressLens = R.lensProp('address')
# headLens = R.lensIndex(0)
dogLens = R.lensPath(['pets', 'dog'])


class TestLens(unittest.TestCase):
  def test_may_be_applie_to_a_lens_created_by_lensPath(self):
    self.assertEqual('joker', R.view(dogLens, alice))

  def test_may_be_applied_to_a_lens_created_by_lensProp(self):
    pass


if __name__ == '__main__':
  unittest.main()
