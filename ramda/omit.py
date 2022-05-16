import copy

from .keys import keys
from .private._curry2 import _curry2


def inner_omit(names, obj):
  """
  case 1: obj is dict
  case 2: obj is object
  """
  if isinstance(obj, dict):
    res = {}
    for key in obj:
      if key not in names:
        res[key] = obj[key]
    return res
  res = copy.copy(obj)
  for key in keys(obj):
    if key in names:
      delattr(res, key)
  return res


omit = _curry2(inner_omit)
