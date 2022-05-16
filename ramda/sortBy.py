from functools import cmp_to_key

from .private._curry2 import _curry2


def inner_sortBy(fn, arr):
  def comparator(a, b):
    aa = fn(a)
    bb = fn(b)
    if aa < bb:
      return -1
    if aa > bb:
      return 1
    return 0
  return sorted(arr, key=cmp_to_key(comparator))


sortBy = _curry2(inner_sortBy)
