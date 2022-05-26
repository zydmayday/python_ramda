from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xfindLast import _xfindLast


def inner_findLast(fn, arr):
  idx = len(arr) - 1
  while idx >= 0:
    if fn(arr[idx]):
      return arr[idx]
    idx -= 1
  return None

findLast = _curry2(_dispatchable([], _xfindLast, inner_findLast))
