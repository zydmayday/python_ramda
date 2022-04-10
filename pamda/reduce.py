from .private._curry3 import _curry3
from .private._isFunction import _isFunction
from .private._xReduce import _xReduce
from .private._xwrap import _xwrap


def inner_reduce(xf, acc, arr):
  return _xReduce(_xwrap(xf) if _isFunction(xf) else xf, acc, arr)

reduce = _curry3(inner_reduce)
