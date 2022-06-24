from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XFind(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f
    self.found = False

  def result(self, result):
    if not self.found:
      result = getAttribute(self.xf, '@@transducer/step')(result, None)
    return self.xf.get('@@transducer/result')(result)

  def step(self, result, _input):
    if self.f(_input):
      self.found = True
      result = _reduced(getAttribute(self.xf, '@@transducer/step')(result, _input))
    return result


def _xfind(f): return lambda xf: XFind(f, xf)
