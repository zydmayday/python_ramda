from ._helper import getAttribute
from ._xfBase import XfBase


class XTap(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f

  def step(self, result, _input):
    self.f(_input)
    return getAttribute(self.xf, '@@transducer/step')(result, _input)


def _xtap(f): return lambda xf: XTap(f, xf)
