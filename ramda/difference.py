from math import isnan
from numbers import Number

from .equals import equals
from .find import find
from .private._curry2 import _curry2


def inner_difference(first, second):
  out = []
  idx = 0
  toFilterOut = set()
  for item in second:
    toFilterOut.add(item)
  firstLen = len(first)
  while idx < firstLen:
    if isinstance(first[idx], Number) and isnan(first[idx]):
      if not find(isnan, list(toFilterOut)):
        toFilterOut.add(first[idx])
        out.append(first[idx])
    elif not find(equals(first[idx]), list(toFilterOut)):
      toFilterOut.add(first[idx])
      out.append(first[idx])
    idx += 1
  return out


difference = _curry2(inner_difference)
