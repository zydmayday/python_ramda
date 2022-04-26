from .clone import clone
from .private._curry1 import _curry1
from .private._helper import getAttribute
from .private._isArray import _isArray
from .private._isDict import _isDict
from .private._isFunction import _isFunction
from .private._isSet import _isSet
from .private._isString import _isString


def inner_empty(x):
  if x is not None and _isFunction(getAttribute(x, 'fantasy-land/empty')):
    return getAttribute(x, 'fantasy-land/empty')()
  if x is not None and _isFunction(getAttribute(x, 'empty')):
    return getAttribute(x, 'empty')()
  if _isArray(x):
    return []
  if _isString(x):
    return ''
  if _isDict(x):
    return {}
  if _isSet(x):
    return set()
  if x is not None:
    # by default, we will not empty other types for now.
    return clone(x)
  return None


empty = _curry1(inner_empty)
