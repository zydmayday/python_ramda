from .equals import equals
from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isArray import _isArray
from .private._isFunction import _isFunction


def inner_lastIndexOf(target, xs):
  if _isFunction(getAttribute(xs, 'lastIndexOf')) and not _isArray(xs):
    return xs.lastIndexOf(target)
  idx = len(xs) - 1
  while idx >= 0:
    if equals(xs[idx], target):
      return idx
    idx -= 1
  return -1


lastIndexOf = _curry2(inner_lastIndexOf)
