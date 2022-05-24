from .private._checkForMethod import _checkForMethod
from .private._curry2 import _curry2


def inner_forEach(fn, arr):
  length = len(arr)
  idx = 0
  while idx < length:
    fn(arr[idx])
    idx += 1
  return arr


forEach = _curry2(_checkForMethod('forEach', inner_forEach))
