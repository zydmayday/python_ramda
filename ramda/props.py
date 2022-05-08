from .map import map
from .path import path
from .private._curry2 import _curry2


def inner_props(ps, obj):
  return map(lambda p: path([p], obj), ps)


props = _curry2(inner_props)
