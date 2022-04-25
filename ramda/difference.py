from math import isnan

from .equals import equals
from .find import find
from .private._curry2 import _curry2
from .private._isNumber import _isNumber
from .private._Set import _Set


def inner_difference(first, second):
  out = []
  idx = 0
  toFilterOut = _Set()
  for item in second:
    toFilterOut.add(item)
  firstLen = len(first)

  while idx < firstLen:
    if toFilterOut.add(first[idx]):
      out.append(first[idx])
    idx += 1

  return out


difference = _curry2(inner_difference)
