from .private._curry1 import _curry1
from .private._isString import _isString
from .private._quote import _quote


def inner_toString(val):
  """
  TODO: dict, set, list, tuple, function, object
  TODO: regex, date if needed
  """
  if _isString(val):
    return _quote(val)
  return str(val)


toString = _curry1(inner_toString)
