from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._includesWith import _includesWith
from .private._xuniqWith import _xuniqWith


def inner_uniqWith(pred, arr):
  idx = 0
  length = len(arr)
  result = []
  while idx < length:
    item = arr[idx]
    if not _includesWith(pred, item, result):
      result.append(item)
    idx += 1
  return result


uniqWith = _curry2(_dispatchable([], _xuniqWith, inner_uniqWith))
