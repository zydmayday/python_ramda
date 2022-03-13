
from inspect import getfullargspec, signature

from pamda.curryN import curryN


def curry(fn):
  fullargspec = getfullargspec(fn)
  n = len(fullargspec.args)
  return curryN(n, fn)
