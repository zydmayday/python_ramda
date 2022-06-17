from .private._curry2 import _curry2


def inner_zipObj(keys, values):
  return dict(zip(keys, values))


zipObj = _curry2(inner_zipObj)
