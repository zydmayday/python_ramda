from .private._curry2 import _curry2


def inner_divide(a, b):
  return a / b


divide = _curry2(inner_divide)
