from pamda.private._curry1 import _curry1


def inner_tail(arr):
  return arr[1:]


tail = _curry1(inner_tail)
