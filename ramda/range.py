from .private._curry2 import _curry2
from .private._isNumber import _isNumber


def inner_range(frm, to):
  if not (_isNumber(frm) and _isNumber(to)):
    raise TypeError('Both arguments to range must be numbers')
  result = []
  n = frm
  while n < to:
    result.append(n)
    n += 1
  return result


# pylint: disable=redefined-builtin
range = _curry2(inner_range)
