from .private._curry2 import _curry2
from .private._isInteger import _isInteger


def inner_mathMod(m, p):
  if not _isInteger(m):
    return float('nan')
  if not _isInteger(p) or p < 1:
    return float('nan')
  return m % p


mathMod = _curry2(inner_mathMod)
