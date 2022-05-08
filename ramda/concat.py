from .private._curry2 import _curry2
from .private._helper import getAttribute
from .private._isArray import _isArray
from .private._isFunction import _isFunction
from .private._isString import _isString
from .toString import toString


def inner_concat(a, b):
  if _isArray(a):
    if _isArray(b):
      return a + b
    raise Exception(f"{toString(b)} is not an array")
  if _isString(a):
    if _isString(b):
      return a + b
    raise Exception(f"{toString(b)} is not a string")
  if a is not None and _isFunction(getAttribute(a, 'fantasy-land/concat')):
    return a.get('fantasy-land/concat')(b)
  if a is not None and _isFunction(a.concat):
    return a.concat(b)
  raise Exception(f'{a} does not have a method named "concat" or "fantasy-land/concat"')


concat = _curry2(inner_concat)
