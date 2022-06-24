from ._helper import getAttribute
from ._includesWith import _includesWith
from ._xfBase import XfBase


class XUniqWith(XfBase):
  def __init__(self, pred, xf):
    super().__init__(xf)
    self.pred = pred
    self.items = []

  def step(self, result, _input):
    if _includesWith(self.pred, _input, self.items):
      return result
    self.items.append(_input)
    return getAttribute(self.xf, '@@transducer/step')(result, _input)


def _xuniqWith(pred): return lambda xf: XUniqWith(pred, xf)
