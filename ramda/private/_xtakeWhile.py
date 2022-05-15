from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XTakeWhile(XfBase):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f

  def step(self, result, input):
    if self.f(input):
      return getAttribute(self.xf, '@@transducer/step')(result, input)
    else:
      return _reduced(result)


def _xtakeWhile(f): return lambda xf: XTakeWhile(f, xf)
