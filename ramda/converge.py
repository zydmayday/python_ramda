from .curryN import curryN
from .Max import Max
from .private._curry2 import _curry2
from .private._inspect import funcArgsLength, getArgsToUse
from .private._map import _map
from .reduce import reduce


def inner_converge(after, fns):
  def wrapper(*args):
    return after(*_map(lambda fn: fn(*getArgsToUse(fn, args)), fns))
  arity = reduce(Max, 0, _map(funcArgsLength, fns))
  return curryN(arity, wrapper)


converge = _curry2(inner_converge)
converge.__name__ = 'converge'
