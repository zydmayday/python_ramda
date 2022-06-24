from ._helper import getAttribute
from ._xfBase import XfBase


class XMap(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f

  def step(self, result, _input):
    return getAttribute(self.xf, '@@transducer/step')(result, self.f(_input))


def _xmap(f): return lambda xf: XMap(f, xf)
