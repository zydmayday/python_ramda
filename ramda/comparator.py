from .private._curry1 import _curry1


def inner_comparator(pred):
  def comparator_wrapper(a, b):
    if pred(a, b):
      return -1
    if pred(b, a):
      return 1
    return 0
  return comparator_wrapper


comparator = _curry1(inner_comparator)
