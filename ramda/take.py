from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xtake import _xtake
from .slice import slice


def inner_take(n, xs):
  return slice(0, None if n < 0 else n, xs)


take = _curry2(_dispatchable(['take'], _xtake, inner_take))
