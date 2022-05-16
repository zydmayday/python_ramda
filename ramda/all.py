from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xall import _xall


def inner_all(fn, arr):
  idx = 0
  while idx < len(arr):
    if not fn(arr[idx]):
      return False
    idx += 1
  return True

# pylint: disable=redefined-builtin
all = _curry2(_dispatchable(['all'], _xall, inner_all))
