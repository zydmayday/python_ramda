from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XTakeWhile(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f

  def step(self, result, _input):
    if self.f(_input):
      return getAttribute(self.xf, '@@transducer/step')(result, _input)
    return _reduced(result)


def _xtakeWhile(f): return lambda xf: XTakeWhile(f, xf)
