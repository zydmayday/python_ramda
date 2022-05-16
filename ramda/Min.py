from .private._curry2 import _curry2
from .toString import toString


def inner_min(a, b):
  if a == b:
    return a

  # pylint: disable=unidiomatic-typecheck
  if type(a) != type(b):
    strA = str(a)
    strB = str(b)
    return a if strA < strB else b

  def safeMin(x, y):
    if (x > y) != (y > x):
      return x if x < y else y
    return None
  minByValue = safeMin(a, b)
  if minByValue is not None:
    return minByValue

  stringA = toString(a)
  minByStringValue = safeMin(stringA, toString(b))
  if minByStringValue is not None:
    return a if minByStringValue == stringA else b
  return a


Min = _curry2(inner_min)
