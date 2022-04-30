from .private._curry2 import _curry2
from .toString import toString


def inner_max(a, b):
  if a == b:
    return b

  if type(a) != type(b):
    strA = str(a)
    strB = str(b)
    return a if strA > strB else b

  def safeMax(x, y):
    if (x > y) != (y > x):
      return x if x > y else y
    return None
  maxByValue = safeMax(a, b)
  if maxByValue is not None:
    return maxByValue

  # maxByType = safeMax(type(a), type(b))
  # if maxByType is not None:
  #   return a if maxByType == type(a) else b

  stringA = toString(a)
  maxByStringValue = safeMax(stringA, toString(b))
  if maxByStringValue is not None:
    return a if maxByStringValue == stringA else b
  return b


Max = _curry2(inner_max)
