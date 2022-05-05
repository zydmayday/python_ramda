from .private._curry2 import _curry2


def inner_or(a, b):
  return a or b


Or = _curry2(inner_or)
