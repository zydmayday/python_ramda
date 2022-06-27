from .map import map
from .Max import Max
from .private._arity import _arity
from .private._curry1 import _curry1
from .private._inspect import funcArgsLength, getArgsToUse
from .reduce import reduce


def inner_cond(pairs):
  arity = reduce(
      Max, 0, map(lambda pair: funcArgsLength(pair[0]), pairs)
  )

  def wrapper(*args):
    idx = 0
    while idx < len(pairs):
      pred = pairs[idx][0]
      argsToUse = getArgsToUse(pred, args)
      if pred(*argsToUse):
        return pairs[idx][1](*args)
      idx += 1
  return _arity(arity, wrapper)


cond = _curry1(inner_cond)
