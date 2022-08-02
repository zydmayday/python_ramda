from .curryN import curryN
from .private._curry3 import _curry3
from .private._inspect import funcArgsLength


def inner_ifElse(condition, onTrue, onFalse):
  def _ifElse(*args):
    if condition(*args):
      return onTrue(*args)
    return onFalse(*args)
  return curryN(max(funcArgsLength(condition), funcArgsLength(onTrue), funcArgsLength(onFalse)), _ifElse)


ifElse = _curry3(inner_ifElse)
