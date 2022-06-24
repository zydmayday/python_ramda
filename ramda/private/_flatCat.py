from ._forceReduced import _forceReduced
from ._helper import getAttribute
from ._isArrayLike import _isArrayLike
from ._xArrayReduce import _xArrayReduce
from ._xfBase import XfBase
from ._xReduce import _xReduce


class XPreservingReduced(XfBase):
  def step(self, result, _input):
    ret = getAttribute(self.xf, '@@transducer/step')(result, _input)
    if getAttribute(ret, '@@transducer/reduced'):
      return _forceReduced(ret)
    return ret


class XFlatCat(XfBase):
  def __init__(self, xf):
    super().__init__(XPreservingReduced(xf))


  def step(self, result, _input):
    if not _isArrayLike(_input):
      return _xArrayReduce(self.xf, result, [_input])
    return _xReduce(self.xf, result, _input)


def _flatCat(xf): return XFlatCat(xf)
