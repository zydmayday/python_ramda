
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/toString.js
"""


class TestToString(unittest.TestCase):
  def test_returns_the_string_representation_of_None(self):
    self.assertEqual('None', R.toString(None))

  def test_returns_the_string_representation_of_a_Boolean_primitive(self):
    self.assertEqual('True', R.toString(True))
    self.assertEqual('False', R.toString(False))

  def test_returns_the_string_representation_of_a_number_primitive(self):
    self.assertEqual('0', R.toString(0))
    self.assertEqual('0', R.toString(-0))
    self.assertEqual('0.0', R.toString(0.0))
    self.assertEqual('-0.0', R.toString(-0.0))
    self.assertEqual('1.23', R.toString(1.23))
    self.assertEqual('-1.23', R.toString(-1.23))
    self.assertEqual('1e+23', R.toString(1e+23))
    self.assertEqual('-1e+23', R.toString(-1e+23))
    self.assertEqual('1e-23', R.toString(1e-23))
    self.assertEqual('-1e-23', R.toString(-1e-23))
    self.assertEqual('inf', R.toString(float('inf')))
    self.assertEqual('-inf', R.toString(float('-inf')))
    self.assertEqual('nan', R.toString(float('nan')))

  def test_returns_the_string_representation_of_a_string_primitive(self):
    self.assertEqual('"abc"', R.toString('abc'))
    self.assertEqual('"x \\"y\\" z"', R.toString('x "y" z'))
    self.assertEqual('"\' \'"', R.toString("' '"))
    self.assertEqual('"\\" \\""', R.toString('" "'))
    self.assertEqual('"\\b \\b"', R.toString('\b \b'))
    self.assertEqual('"\\f \\f"', R.toString('\f \f'))
    self.assertEqual('"\\n \\n"', R.toString('\n \n'))
    self.assertEqual('"\\r \\r"', R.toString('\r \r'))
    self.assertEqual('"\\t \\t"', R.toString('\t \t'))
    self.assertEqual('"\\v \\v"', R.toString('\v \v'))
    self.assertEqual('"\\0 \\0"', R.toString('\0 \0'))
    self.assertEqual('"\\\\ \\\\"', R.toString('\\ \\'))

  # TODO: add other tests

if __name__ == '__main__':
  unittest.main()
