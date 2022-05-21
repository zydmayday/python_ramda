from .private._curry2 import _curry2


def inner_xprod(a, b):
  idx = 0
  ilen = len(a)
  jlen = len(b)
  result = []
  while idx < ilen:
    j = 0
    while j < jlen:
      result.append([a[idx], b[j]])
      j += 1
    idx += 1
  return result


xprod = _curry2(inner_xprod)
