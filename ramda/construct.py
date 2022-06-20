from .constructN import constructN
from .Max import Max
from .private._curry1 import _curry1
from .private._inspect import funcArgsLength


def inner_construct(Fn):
  # should ignore first argument
  n = Max(0, funcArgsLength(Fn.__init__) - 1)
  return constructN(n, Fn)


construct = _curry1(inner_construct)
