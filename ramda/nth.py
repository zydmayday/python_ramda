from .private._curry2 import _curry2
from .private._isString import _isString


def inner_nth(offset, arr):
  idx = len(arr) + offset if offset < 0 else offset
  if _isString(arr):
    if 0 <= idx < len(arr):
      return arr[idx]
    return ''
  if 0 <= idx < len(arr):
    return arr[idx]
  return None


nth = _curry2(inner_nth)
