from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xfindLastIndex import _xfindLastIndex


def inner_findLastIndex(fn, arr):
  idx = len(arr) - 1
  while idx >= 0:
    if fn(arr[idx]):
      return idx
    idx -= 1
  return -1


findLastIndex = _curry2(_dispatchable([], _xfindLastIndex, inner_findLastIndex))
