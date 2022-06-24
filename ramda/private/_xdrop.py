from ._helper import getAttribute
from ._xfBase import XfBase


class XDrop(XfBase):
  def __init__(self, n, xf):
    super().__init__(xf)
    self.n = n

  def step(self, result, _input):
    if self.n > 0:
      self.n -= 1
      return result
    return getAttribute(self.xf, '@@transducer/step')(result, _input)


def _xdrop(n): return lambda xf: XDrop(n, xf)
