from .nth import nth
from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isInteger import _isInteger


def inner_prop(p, obj):
  if obj is None:
    return None
  return nth(p, obj) if _isInteger(p) else getAttribute(obj, p)


prop = _curry2(inner_prop)
