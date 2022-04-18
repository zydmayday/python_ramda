from .private._curry1 import _curry1


def inner_comparator(pred):
  def comparator(a, b):
    if pred(a, b):
      return -1
    elif pred(b, a):
      return 1
    else:
      return 0
  return comparator


comparator = _curry1(inner_comparator)
