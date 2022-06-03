from collections.abc import Iterable

from ._helper import getAttribute
from ._isArrayLike import _isArrayLike
from ._isFunction import _isFunction


def _createReduce(arrayReduce, methodReduce, iterableReduce):
  def _reduce(xf, acc, arr):
    if arr is None:
      return acc
    if _isArrayLike(arr):
      return arrayReduce(xf, acc, arr)
    if _isFunction(getAttribute(arr, 'fantasy-land/reduce')):
      return methodReduce(xf, acc, arr, 'fantasy-land/reduce')
    if isinstance(arr, Iterable):
      return iterableReduce(xf, acc, arr)
    if _isFunction(getattr(arr, 'reduce', None)):
      return methodReduce(xf, acc, arr, 'reduce')
    raise Exception('reduce: list must be array or iterable')
  return _reduce
