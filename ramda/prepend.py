from .private._concat import _concat
from .private._curry2 import _curry2


def inner_prepend(el, arr):
  return _concat([el], arr)


prepend = _curry2(inner_prepend)
