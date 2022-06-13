from .map import map
from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._isFunction import _isFunction
from .private._makeFlat import _makeFlat
from .private._xchain import _xchain


def inner_chain(fn, monad):
  if _isFunction(monad):
    def wrapper(x):
      return fn(monad(x))(x)
    return wrapper
  return _makeFlat(False)(map(fn, monad))


chain = _curry2(_dispatchable(['fantasy-land/chain', 'chain'], _xchain, inner_chain))
