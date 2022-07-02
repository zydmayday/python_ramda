
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/T.js
"""

test = '\x09\x0A\x0B\x0C\x0D\x20\xA0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000\u2028\u2029\uFEFFHello, World!\x09\x0A\x0B\x0C\x0D\x20\xA0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000\u2028\u2029\uFEFF'

class TestT(unittest.TestCase):
  def test_trims_a_string(self):
    self.assertEqual('xyz', R.trim('   xyz   '))

  def test_does_not_trim_the_zero_width_space(self):
    self.assertEqual('\u200b', R.trim('\u200b'))
    self.assertEqual(1, len(R.trim('\u200b')))


if __name__ == '__main__':
  unittest.main()
