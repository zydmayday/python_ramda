from pamda.private._curry1 import _curry1


def inner_reverse(arr):
  return arr[::-1]


reverse = _curry1(inner_reverse)
