from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._Set import _Set
from .private._xuniqBy import _xuniqBy


def inner_uniqBy(fn, arr):
  _set = _Set()
  result = []
  idx = 0

  while idx < len(arr):
    item = arr[idx]
    appliedItem = fn(item)
    if _set.add(appliedItem):
      result.append(item)
    idx += 1
  return result


uniqBy = _curry2(_dispatchable(['uniqBy'], _xuniqBy, inner_uniqBy))
