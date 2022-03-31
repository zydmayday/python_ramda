from ._helper import getAttribute
from ._xfBase import XfBase


class XMap(XfBase):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f

  def step(self, result, input):
    return getAttribute(self.xf, '@@transducer/step')(result, self.f(input))


def _xmap(f): return lambda xf: XMap(f, xf)
