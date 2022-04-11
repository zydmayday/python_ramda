from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XFind(XfBase):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f
    self.found = False

  def result(self, result):
    if not self.found:
      result = getAttribute(self.xf, '@@transducer/step')(result, None)
    return self.xf.get('@@transducer/result')(result)

  def step(self, result, input):
    if self.f(input):
      self.found = True
      result = _reduced(getAttribute(self.xf, '@@transducer/step')(result, input))
    return result


def _xfind(f): return lambda xf: XFind(f, xf)
