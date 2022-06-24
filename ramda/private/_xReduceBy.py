from ._clone import _clone
from ._has import _has
from ._helper import getAttribute
from ._xfBase import XfBase


class XReduceBy(XfBase):
  def __init__(self, valueFn, valueAcc, keyFn, xf):
    super().__init__(xf)
    self.valueFn = valueFn
    self.valueAcc = valueAcc
    self.keyFn = keyFn
    self.inputs = {}

  def result(self, result):
    for key in self.inputs:
      if _has(self.inputs, key):
        result = getAttribute(self.xf, '@@transducer/step')(result, self.inputs[key])
        if getAttribute(result, '@@transducer/reduced'):
          result = getAttribute(result, '@@transducer/value')
          break
    self.inputs = None
    return getAttribute(self.xf, '@@transducer/result')(result)

  def step(self, result, _input):
    key = self.keyFn(_input)
    self.inputs[key] = getAttribute(self.inputs, key) or [key, _clone(self.valueAcc, deep=False)]
    self.inputs[key][1] = self.valueFn(self.inputs[key][1], _input)
    return result


def _xReduceBy(valueFn, valueAcc, keyFn): return lambda xf: XReduceBy(valueFn, valueAcc, keyFn, xf)
