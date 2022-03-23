from mimetypes import init

from ._reduced import _reduced
from ._X import X


class XAll(X):
  def __init__(self, f, xf):
    self.xf = xf
    self.f = f
    self.all = True

  def init(self):
    return self.get('@@transducer/init')

  def result(self, result):
    if self.all:
      result = self.xf.get('@@transducer/step')(result, True)
    return self.xf.get('@@transducer/result')(result)

  def step(self, result, input):
    if not self.f(input):
      self.all = False
      result = _reduced(self.xf.get('@@transducer/step')(result, False))
    return result



def _xall(f):
  def inner(xf):
    return XAll(f, xf)
  return inner
