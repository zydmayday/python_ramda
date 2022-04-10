from .private._concat import _concat
from .private._curry2 import _curry2


def inner_append(el, arr):
  return _concat(arr, [el])


append = _curry2(inner_append)
