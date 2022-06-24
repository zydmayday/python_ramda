from ._helper import getAttribute
from ._xfBase import XfBase


class XFindLast(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f
    self.last = None

  def result(self, result):
    return getAttribute(self.xf, '@@transducer/result')(getAttribute(self.xf, '@@transducer/step')(result, self.last))

  def step(self, result, _input):
    if self.f(_input):
      self.last = _input
    return result


def _xfindLast(f): return lambda xf: XFindLast(f, xf)
