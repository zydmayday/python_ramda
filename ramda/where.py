from .private._curry2 import _curry2
from .private._has import _has
from .private._helper import getAttribute


def inner_where(spec, testObj):
  for prop in spec:
    if _has(spec, prop) and not spec[prop](getAttribute(testObj, prop)):
      return False
  return True


where = _curry2(inner_where)
