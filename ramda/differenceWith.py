from .private._curry3 import _curry3
from .private._includesWith import _includesWith


def inner_differenceWith(pred, first, second):
  out = []
  idx = 0
  firstLength = len(first)
  while idx < firstLength:
    if (not _includesWith(pred, first[idx], second)) and (not _includesWith(pred, first[idx], out)):
      out.append(first[idx])
    idx += 1
  return out


differenceWith = _curry3(inner_differenceWith)
