from .curryN import curryN
from .private._curry2 import _curry2


def inner_useWith(fn, transformers):
  def wrapper(*arguments):
    args = []
    idx = 0
    while idx < len(transformers):
      args.append(transformers[idx](arguments[idx]))
      idx += 1
    return fn(*(args + list(arguments[len(transformers):])))
  return curryN(len(transformers), wrapper)


useWith = _curry2(inner_useWith)
