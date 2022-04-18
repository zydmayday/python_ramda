from .private._clone import _clone
from .private._curryN import _curryN
from .private._dispatchable import _dispatchable
from .private._has import _has
from .private._helper import getAttribute
from .private._reduced import _reduced
from .private._xReduce import _xReduce
from .private._xReduceBy import _xReduceBy
from .private._xwrap import _xwrap


def inner_reduceBy(valueFn, valueAcc, keyFn, arr):
  def inner_xwrap(acc, elt):
    key = keyFn(elt)
    value = valueFn(acc[key] if _has(acc, key) else _clone(valueAcc, deep=False), elt)

    if value and getAttribute(value, '@@transducer/reduced'):
      return _reduced(acc)

    acc[key] = value
    return acc
  xf = _xwrap(inner_xwrap)
  return _xReduce(xf, {}, arr)

reduceBy = _curryN(4, [], _dispatchable([], _xReduceBy, inner_reduceBy))
