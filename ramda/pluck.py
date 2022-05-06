from .map import map
from .private._curry2 import _curry2
from .prop import prop


def inner_pluck(p, arr):
  return map(prop(p), arr)


pluck = _curry2(inner_pluck)
