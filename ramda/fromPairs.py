from .private._curry1 import _curry1


def inner_fromPairs(pairs):
  result = {}
  idx = 0
  while idx < len(pairs):
    result[pairs[idx][0]] = pairs[idx][1]
    idx += 1
  return result


fromPairs = _curry1(inner_fromPairs)
