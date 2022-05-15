from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xtakeWhile import _xtakeWhile
from .slice import slice


def inner_takeWhile(fn, xs):
  idx = 0
  length = len(xs)
  while idx < length and fn(xs[idx]):
    idx += 1
  return slice(0, idx, xs)


takeWhile = _curry2(_dispatchable(['takeWhile'], _xtakeWhile, inner_takeWhile))
