from pamda.private._curry3 import _curry3


def inner_slice(fromIndex, toIndex, arr):
  return arr[fromIndex:toIndex]


slice = _curry3(inner_slice)
