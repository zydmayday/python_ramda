from ._helper import getAttribute
from ._Set import _Set
from ._xfBase import XfBase


class XUniqBy(XfBase):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f
    self._set = _Set()

  def step(self, result, input):
    if self._set.add(self.f(input)):
      return getAttribute(self.xf, '@@transducer/step')(result, input)
    else:
      return result


def _xuniqBy(f): return lambda xf: XUniqBy(f, xf)
