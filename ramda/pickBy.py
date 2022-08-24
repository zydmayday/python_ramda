from .private._curry2 import _curry2
from .private._inspect import funcArgsLength


def inner_pickBy(test, obj):
  result = {}
  for key in obj:
    if funcArgsLength(test) <= 1:
      if test(obj[key]):
        result[key] = obj[key]
    if funcArgsLength(test) == 2:
      if test(obj[key], key):
        result[key] = obj[key]
    if funcArgsLength(test) == 3:
      if test(obj[key], key, obj):
        result[key] = obj[key]
  return result


pickBy = _curry2(inner_pickBy)
