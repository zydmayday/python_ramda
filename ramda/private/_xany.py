from ._helper import getAttribute
from ._reduced import _reduced
from ._xfBase import XfBase


class XAny(XfBase):
  def __init__(self, f, xf):
    super().__init__(xf)
    self.f = f
    self.any = False

  def result(self, result):
    if not self.any:
      result = getAttribute(self.xf, '@@transducer/step')(result, False)
    return self.xf.get('@@transducer/result')(result)

  def step(self, result, _input):
    if self.f(_input):
      self.any = True
      result = _reduced(getAttribute(self.xf, '@@transducer/step')(result, True))
    return result


def _xany(f): return lambda xf: XAny(f, xf)
