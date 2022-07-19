from .ap import ap
from .curryN import curryN
from .map import map
from .private._arrayReduce import _arrayReduce
from .private._curry2 import _curry2


def inner_liftN(arity, fn):
  lifted = curryN(arity, fn)

  def wrapper(*args):
    args = list(args)
    return _arrayReduce(ap, map(lifted, args[0]), args[1:])
  return curryN(arity, wrapper)


liftN = _curry2(inner_liftN)
