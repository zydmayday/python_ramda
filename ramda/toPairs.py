from .keys import keys
from .private._curry1 import _curry1
from .private._helper import getAttribute


def inner_toPairs(obj):
  pairs = []
  for key in keys(obj):
    pairs.append([key, getAttribute(obj, key)])
  return pairs


toPairs = _curry1(inner_toPairs)
