import unittest

from ramda.private._stepCat import _stepCat

from ..helpers.listXf import listXf


class Test_StepCat(unittest.TestCase):
  def test_fix_code_coverage_error(self):
    self.assertEqual(listXf, _stepCat(listXf))

    with self.assertRaises(Exception):
      _stepCat(None)


if __name__ == '__main__':
  unittest.main()
