from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xfindIndex import _xfindIndex


def inner_findIndex(fn, arr):
  idx = 0
  length = len(arr)
  while idx < length:
    if fn(arr[idx]):
      return idx
    idx += 1
  return -1


findIndex = _curry2(_dispatchable([], _xfindIndex, inner_findIndex))
