from .curryN import curryN
from .private._curry1 import _curry1
from .private._inspect import funcArgsLength


def inner_flip(fn):
  def wrapper(a, b, *args):
    return fn(b, a, *args)
  return curryN(funcArgsLength(fn), wrapper)


flip = _curry1(inner_flip)
