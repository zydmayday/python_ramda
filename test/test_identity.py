import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/identity.js
"""


class TestIdentity(unittest.TestCase):
  def test_returns_its_first_argument(self):
    self.assertEqual(None, R.identity(None))
    self.assertEqual('foo', R.identity('foo'))
    self.assertEqual('foo', R.identity('foo', 'bar'))


if __name__ == '__main__':
  unittest.main()
