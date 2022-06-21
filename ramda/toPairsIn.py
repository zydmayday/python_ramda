from .keysIn import keysIn
from .private._curry1 import _curry1
from .private._helper import getAttribute


def inner_toPairsIn(obj):
  pairs = []
  for key in keysIn(obj):
    pairs.append([key, getAttribute(obj, key)])
  return pairs


toPairsIn = _curry1(inner_toPairsIn)
