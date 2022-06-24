from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XTake(XfBase):
  def __init__(self, n, xf):
    super().__init__(xf)
    self.n = n
    self.i = 0

  def step(self, result, _input):
    self.i += 1
    ret = result if self.n == 0 else getAttribute(self.xf, '@@transducer/step')(result, _input)
    if self.n >= 0 and self.i >= self.n:
      return _reduced(ret)
    return ret


def _xtake(n): return lambda xf: XTake(n, xf)
