from .private._curry3 import _curry3


def inner_insert(idx, elt, arr):
  idx = idx if 0 <= idx < len(arr) else len(arr)
  return arr[:idx] + [elt] + arr[idx:]


insert = _curry3(inner_insert)
