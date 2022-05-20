from .keys import keys
from .private._curry1 import _curry1
from .private._helper import getAttribute


def inner_values(obj):
  props = keys(obj)
  length = len(props)
  vals = []
  idx = 0
  while idx < length:
    val = getAttribute(obj, props[idx])
    vals.append(val)
    idx += 1
  return vals


values = _curry1(inner_values)
