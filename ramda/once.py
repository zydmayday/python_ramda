from .private._arity import _arity
from .private._curry1 import _curry1
from .private._inspect import funcArgsLength


def inner_once(fn):
  called = False
  result = None

  def wrapper(*args):
    nonlocal called, result
    if called:
      return result
    called = True
    result = fn(*args)
    return result
  return _arity(funcArgsLength(fn), wrapper)


once = _curry1(inner_once)
