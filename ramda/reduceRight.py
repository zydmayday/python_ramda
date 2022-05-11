from .private._curry3 import _curry3
from .private._helper import getAttribute


def inner_reduceRight(fn, acc, arr):
  idx = len(arr) - 1
  while idx >= 0:
    acc = fn(arr[idx], acc)
    if acc and getAttribute(acc, '@@transducer/reduced'):
      acc = getAttribute(acc, '@@transducer/value')
      break
    idx -= 1
  return acc


reduceRight = _curry3(inner_reduceRight)
