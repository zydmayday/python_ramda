from ._helper import getAttribute
from ._xfBase import XfBase


class XFindLastIndex(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f
    self.idx = -1
    self.lastIdx = -1

  def result(self, result):
    return getAttribute(self.xf, '@@transducer/result')(getAttribute(self.xf, '@@transducer/step')(result, self.lastIdx))

  def step(self, result, _input):
    self.idx += 1
    if self.f(_input):
      self.lastIdx = self.idx
    return result


def _xfindLastIndex(f): return lambda xf: XFindLastIndex(f, xf)
