from math import isnan

import ramda as R

from ._helper import getAttribute
from ._isFunction import _isFunction
from ._isNumber import _isNumber


def _indexOf(arr, a, idx):
  if _isFunction(getAttribute(arr, 'indexOf')):
    if _isNumber(a) and isnan(a):
      while idx < len(arr):
        if isnan(arr[idx]):
          return idx
        idx += 1
    return arr.indexOf(a, idx)

  while idx < len(arr):
    if R.equals(arr[idx], a):
      return idx
    idx += 1
  return -1
