from typing import Iterable

from ._xwrap import _xwrap


def _reduce(fn, acc, arr):
  """
  Support list / iterable for now.
  TODO: Support method reduce
  """
  if callable(fn):
    fn = _xwrap(fn)
  if arr is None:
    return acc
  if isinstance(arr, list):
    return _arrayReduce(fn, acc, arr)
  if isinstance(arr, Iterable):
    return _iterableReduce(fn, acc, arr)
  raise Exception('reduce: list must be array or iterable')


def _arrayReduce(xf, acc, arr):
  idx = 0
  n = len(arr)
  while idx < n:
    acc = xf.get('@@transducer/step')(acc, arr[idx])
    if acc and isinstance(acc, dict) and acc.get('@@transducer/reduced', False):
      acc = acc.get('@@transducer/value')
      break
    idx += 1
  return xf.get('@@transducer/result')(acc)


def _iterableReduce(xf, acc, iter):
  while True:
    try:
      acc = xf.get('@@transducer/step')(acc, next(iter))
      if acc and isinstance(acc, dict) and acc.get('@@transducer/reduced', False):
        acc = acc.get('@@transducer/value')
        break
    except StopIteration:
      break
  return xf.get('@@transducer/result')(acc)
