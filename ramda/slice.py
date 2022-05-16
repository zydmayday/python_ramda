from .private._checkForMethod import _checkForMethod
from .private._curry3 import _curry3


def inner_slice(fromIndex, toIndex, arr):
  if toIndex is None:
    return arr[fromIndex:]
  return arr[fromIndex:toIndex]


# pylint: disable=redefined-builtin
slice = _curry3(_checkForMethod('slice', inner_slice))
