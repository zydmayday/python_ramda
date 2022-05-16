from ._helper import getAttribute
from ._xfBase import XfBase


class XFilter(XfBase):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f

  def step(self, result, _input):
    return getAttribute(self.xf, '@@transducer/step')(result, _input) if self.f(_input) else result

def _xfilter(f): return lambda xf: XFilter(f, xf)
