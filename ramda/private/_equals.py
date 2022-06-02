from math import isnan

from ._helper import getAttribute
from ._isArrayLike import _isArrayLike
from ._isFunction import _isFunction
from ._isNumber import _isNumber


def _equals(a, b):
  if _isNumber(a) and isnan(a) and _isNumber(b) and isnan(b):
    return True
  # pylint: disable=unidiomatic-typecheck
  if type(a) != type(b):
    return False
  if isinstance(a, BaseException):
    # Exception
    return str(a) == str(b)
  if _isArrayLike(a) and _isArrayLike(b):
    # Array-like
    if len(a) != len(b):
      return False
    return all(_equals(a[i], b[i]) for i in range(len(a)))
  if _isFunction(getAttribute(a, 'equals')) and _isFunction(getAttribute(b, 'equals')):
    # dispatch to objects' own equals method
    return a.equals(b) and b.equals(a)
  # default equals
  return a == b
