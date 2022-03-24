from pamda.private._helper import getAttribute

from ._reduced import _reduced
from ._xfBase import XfBase


class XAny(XfBase):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f
    self.any = False

  def result(self, result):
    if not self.any:
      result = getAttribute(self.xf, '@@transducer/step')(result, False)
    return self.xf.get('@@transducer/result')(result)

  def step(self, result, input):
    if self.f(input):
      self.any = True
      result = _reduced(getAttribute(self.xf, '@@transducer/step')(result, True))
    return result



def _xany(f):
  def inner(xf):
    return XAny(f, xf)
  return inner