from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XAll(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f
    self.all = True

  def result(self, result):
    if self.all:
      result = getAttribute(self.xf, '@@transducer/step')(result, True)
    return self.xf.get('@@transducer/result')(result)

  def step(self, result, _input):
    if not self.f(_input):
      self.all = False
      result = _reduced(getAttribute(self.xf, '@@transducer/step')(result, False))
    return result


def _xall(f): return lambda xf: XAll(f, xf)
