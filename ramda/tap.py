from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xtap import _xtap


def inner_tap(fn, x):
  fn(x)
  return x


tap = _curry2(_dispatchable([], _xtap, inner_tap))
