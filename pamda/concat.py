from pamda.private._curry2 import _curry2
from pamda.private._helper import getAttribute
from pamda.private._isArray import _isArray
from pamda.private._isFunction import _isFunction
from pamda.private._isString import _isString


def inner_concat(a, b):
  if _isArray(a):
    if _isArray(b):
      return a + b
    # TODO: Change to R.toString method
    raise Exception(f"{b} is not an array")
  if _isString(a):
    if _isString(b):
      return a + b
    # TODO: Change to R.toString method
    raise Exception(f"{b} is not a string")
  if a is not None and _isFunction(getAttribute(a, 'fantasy-land/concat')):
    return a.get('fantasy-land/concat')(b)
  if a is not None and _isFunction(a.concat):
    return a.concat(b)
  raise Exception(f'{a} does not have a method named "concat" or "fantasy-land/concat"')


concat = _curry2(inner_concat)
