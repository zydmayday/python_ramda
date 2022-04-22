from ._helper import safeLen
from ._isArrayLike import _isArrayLike


def _makeFlat(recursive):
  def flatt(arr):
    result = []
    idx = 0
    ilen = len(arr)

    while idx < ilen:
      if _isArrayLike(arr[idx]):
        value = flatt(arr[idx]) if recursive else arr[idx]
        j = 0
        jlen = safeLen(value)
        while j < jlen:
          result.append(value[j])
          j += 1
      else:
        result.append(arr[idx])
      idx += 1
    return result
  return flatt
