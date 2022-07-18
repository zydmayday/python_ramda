from .isNil import isNil
from .private._curry2 import _curry2
from .private._hasOwn import _hasOwn
from .private._helper import getAttribute


def inner_hasPath(path, obj):
  if len(path) == 0 or isNil(obj):
    return False
  val = obj
  idx = 0
  while idx < len(path):
    if not isNil(val) and _hasOwn(val, path[idx]):
      val = getAttribute(val, path[idx])
      idx += 1
    else:
      return False
  return True


hasPath = _curry2(inner_hasPath)
