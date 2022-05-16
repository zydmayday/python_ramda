from .map import map
from .nth import nth
from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isInteger import _isInteger


def inner_paths(pathsArray, obj):
  def mapWrapper(_paths):
    val = obj
    idx = 0
    while idx < len(_paths):
      if val is None:
        return None
      p = _paths[idx]
      val = nth(p, val) if _isInteger(p) else getAttribute(val, p)
      idx += 1
    return val
  return map(mapWrapper, pathsArray)


paths = _curry2(inner_paths)
