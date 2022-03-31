from functools import cmp_to_key

from .private._curry2 import _curry2


def inner_sort(comparator, arr):
  return sorted(arr, key=cmp_to_key(comparator))


sort = _curry2(inner_sort)
