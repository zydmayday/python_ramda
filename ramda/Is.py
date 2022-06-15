from .private._curry2 import _curry2


def inner_is(Ctor, val):
  if val is None:
    return val is None
  return isinstance(val, Ctor)


Is = _curry2(inner_is)
