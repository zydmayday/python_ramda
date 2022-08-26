from .Min import Min
from .private._curry3 import _curry3


def inner_minBy(f, a, b):
  resultB = f(b)
  return b if Min(f(a), resultB) == resultB else a


minBy = _curry3(inner_minBy)
