from .private._clone import _clone
from .private._curry1 import _curry1
from .private._helper import getAttribute
from .private._isFunction import _isFunction


def inner_clone(value):
  if _isFunction(getAttribute(value, 'clone')):
    return value.clone()
  return _clone(value, True)


clone = _curry1(inner_clone)
