from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._xdrop import _xdrop
from .slice import slice


def inner_drop(n, xs):
  return slice(max(0, n), len(xs), xs)


drop = _curry2(_dispatchable(['drop'], _xdrop, inner_drop))
