from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isFunction import _isFunction


def inner_of(Ctor, val):
  if _isFunction(getAttribute(Ctor, 'fantasy-land/of')):
    return getAttribute(Ctor, 'fantasy-land/of')(val)
  if _isFunction(getAttribute(Ctor, 'of')):
    return getAttribute(Ctor, 'of')(val)
  return [val]


of = _curry2(inner_of)
