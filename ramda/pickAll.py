import copy

from .keys import keys
from .private._curry2 import _curry2


def inner_pickAll(names, obj):
  """
  case 1: obj is dict
  case 2: obj is object
  """
  if isinstance(obj, dict):
    res = {}
    for name in names:
      if name in obj:
        res[name] = obj[name]
      else:
        res[name] = None
    return res
  res = copy.copy(obj)
  for key in keys(obj):
    if key not in names:
      delattr(res, key)
  for name in names:
    if not hasattr(res, name):
      setattr(res, name, None)
  return res


pickAll = _curry2(inner_pickAll)
