from .curryN import curryN
from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isFunction import _isFunction
from .toString import toString


def inner_invoker(arity, method):
  def wrapper(*args):
    target = args[arity]
    if target is not None and _isFunction(getAttribute(target, method)):
      return getAttribute(target, method)(*args[:arity])
    raise TypeError(f'{toString(target)} does not have method {method}')
  return curryN(arity + 1, wrapper)


invoker = _curry2(inner_invoker)
