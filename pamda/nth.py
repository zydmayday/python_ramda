from .private._curry2 import _curry2
from .private._isString import _isString


def inner_nth(offset, arr):
  idx = len(arr) + offset if offset < 0 else offset
  if _isString(arr):
    return arr[idx] if idx < len(arr) and idx >= 0 else ''
  else:
    return arr[idx] if idx < len(arr) and idx >= 0 else None


nth = _curry2(inner_nth)
