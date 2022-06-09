from .map import map
from .private._concat import _concat
from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isFunction import _isFunction
from .private._reduce import _reduce


def inner_ap(applyF, applyX):
  if _isFunction(getAttribute(applyX, 'fantasy-land/ap')):
    return getAttribute(applyX, 'fantasy-land/ap')(applyF)
  if _isFunction(getAttribute(applyF, 'ap')):
    return getAttribute(applyF, 'ap')(applyX)
  if _isFunction(applyF):
    return lambda x: applyF(x)(applyX(x))
  return _reduce(lambda acc, f: _concat(acc, map(f, applyX)), [], applyF)


ap = _curry2(inner_ap)
