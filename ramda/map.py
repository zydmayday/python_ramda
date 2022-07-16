import copy

from .curryN import curryN
from .keys import keys
from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._has import _has
from .private._inspect import funcArgsLength
from .private._isArrayLike import _isArrayLike
from .private._isFunction import _isFunction
from .private._map import _map
from .private._reduce import _reduce
from .private._xmap import _xmap


def inner_map(fn, functor):
  def inner_reduce(acc, key):
    """
    There are 2 cases of functor
    case 1: functor is a dict or an instance with get method
    case 2: functor is an instance of some classes
    """
    if isinstance(functor, dict) or _has(functor, 'get'):
      acc[key] = fn(functor.get(key))
    else:
      setattr(acc, key, fn(getattr(acc, key, None)))
    return acc

  if functor is None:
    raise Exception('Can not work with None')
  if _isFunction(functor):
    return curryN(funcArgsLength(functor), lambda *arguments: fn(functor(*arguments)))
  if _isArrayLike(functor):
    return _map(fn, functor)
  return _reduce(inner_reduce, {} if isinstance(functor, dict) or _has(functor, 'get') else copy.deepcopy(functor), keys(functor))


# pylint: disable=redefined-builtin
map = _curry2(_dispatchable(['fantasy-land/map', 'map'], _xmap, inner_map))
