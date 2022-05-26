from math import isnan

from .private._curry2 import _curry2
from .private._helper import toNumber


def inner_times(fn, n):
  length = toNumber(n)
  idx = 0

  if length < 0 or isnan(length):
    raise ValueError('n must be a non-negative number')
  arr = []
  while idx < length:
    arr.append(fn(idx))
    idx += 1
  return arr


times = _curry2(inner_times)
