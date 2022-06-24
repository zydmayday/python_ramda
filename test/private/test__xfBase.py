import unittest

from ramda.private._xfBase import XfBase

from ..helpers.listXf import listXf


class Test_XfBase(unittest.TestCase):
  def test_fix_code_coverage_error(self):
    xfBase = XfBase(listXf)
    xfBase.step(None, None)


if __name__ == '__main__':
  unittest.main()
