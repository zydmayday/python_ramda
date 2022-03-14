
from pamda.curryN import curryN
from pamda.private._curry1 import _curry1
from pamda.private._helper import funcArgsLength


def _inner_curry(fn):
  return curryN(funcArgsLength(fn), fn)

curry = _curry1(_inner_curry)
