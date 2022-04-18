from .private._concat import _concat
from .private._curry3 import _curry3


def inner_adjust(idx, fn, arr):
  length = len(arr)
  if idx >= length or idx < -length:
    return arr
  _idx = (length + idx) % length
  _arr = _concat(arr)
  _arr[_idx] = fn(arr[_idx])
  return _arr


adjust = _curry3(inner_adjust)
