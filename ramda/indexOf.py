from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._indexOf import _indexOf
from .private._isArray import _isArray
from .private._isFunction import _isFunction


def inner_indexOf(target, xs):
  if _isFunction(getAttribute(xs, 'indexOf')) and not _isArray(xs):
    return xs.indexOf(target)
  return _indexOf(xs, target, 0)


indexOf = _curry2(inner_indexOf)
