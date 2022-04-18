from ._helper import getAttribute
from ._isArrayLike import _isArrayLike
from ._isFunction import _isFunction


def _equals(a, b):
  if type(a) != type(b):
    return False
  if isinstance(a, BaseException):
    # Exception
    return str(a) == str(b)
  if _isArrayLike(a) and _isArrayLike(b):
    # Array-like
    if len(a) != len(b):
      return False
    for i in range(len(a)):
      if not _equals(a[i], b[i]):
        return False
    return True
  if _isFunction(getAttribute(a, 'equals')) and _isFunction(getAttribute(b, 'equals')):
    # dispatch to objects' own equals method
    return a.equals(b) and b.equals(a)
  # default equals
  return a == b
