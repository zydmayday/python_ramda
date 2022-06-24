from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XFindIndex(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f
    self.idx = -1
    self.found = False

  def result(self, result):
    if not self.found:
      result = getAttribute(self.xf, '@@transducer/step')(result, -1)
    return getAttribute(self.xf, '@@transducer/result')(result)

  def step(self, result, _input):
    self.idx += 1
    if self.f(_input):
      self.found = True
      result = _reduced(getAttribute(self.xf, '@@transducer/step')(result, self.idx))
    return result


def _xfindIndex(f): return lambda xf: XFindIndex(f, xf)
