from .isNil import isNil
from .private._curry2 import _curry2
from .private._has import _has


def inner_hasIn(prop, obj):
  if isNil(obj):
    return False
  return _has(obj, prop)


hasIn = _curry2(inner_hasIn)
