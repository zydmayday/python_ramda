from .Max import Max
from .private._curry3 import _curry3


def inner_maxBy(f, a, b):
  resultB = f(b)
  return b if Max(f(a), resultB) == resultB else a


maxBy = _curry3(inner_maxBy)
