from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xfind import _xfind


def inner_find(fn, arr):
  idx = 0
  while idx < len(arr):
    if fn(arr[idx]):
      return arr[idx]
    idx += 1


find = _curry2(_dispatchable(['find'], _xfind, inner_find))
