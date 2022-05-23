from .private._curry3 import _curry3


def inner_zipWith(fn, a, b):
  rv = []
  idx = 0
  length = min(len(a), len(b))
  while idx < length:
    rv.append(fn(a[idx], b[idx]))
    idx += 1
  return rv


zipWith = _curry3(inner_zipWith)
