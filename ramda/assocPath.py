from .isNil import isNil
from .private._assoc import _assoc
from .private._curry3 import _curry3
from .private._has import _has
from .private._isInteger import _isInteger


def inner_assocPath(path, val, obj):
  if len(path) == 0:
    return val
  idx = path[0]
  if len(path) > 1:
    if not isNil(obj) and _has(obj, idx) and isinstance(obj[idx], (dict, list)):
      nextObj = obj[idx]
    elif _isInteger(path[1]):
      nextObj = []
    else:
      nextObj = {}
    val = inner_assocPath(path[1:], val, nextObj)
  return _assoc(idx, val, obj)

assocPath = _curry3(inner_assocPath)
