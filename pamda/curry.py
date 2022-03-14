
from inspect import getfullargspec, signature

from pamda.curryN import curryN
from pamda.private._curry1 import _curry1


def _inner_curry(fn):
  fullargspec = getfullargspec(fn)
  n = len(fullargspec.args)
  return curryN(n, fn)

curry = _curry1(_inner_curry)
