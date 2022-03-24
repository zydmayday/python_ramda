from pamda.private._curry2 import _curry2
from pamda.private._dispatchable import _dispatchable
from pamda.private._xany import _xany


def inner_any(fn, arr):
  idx = 0
  while idx < len(arr):
    if fn(arr[idx]):
      return True
    idx += 1
  return False


any = _curry2(_dispatchable(['any'], _xany, inner_any))
