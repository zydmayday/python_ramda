from .private._curry1 import _curry1
from .private._has import _has
from .private._helper import getAttribute
from .private._inspect import funcArgsLength
from .private._isFunction import _isFunction
from .private._isNumber import _isNumber


def number_or_nan(x):
  if _isNumber(x):
    return x
  return float('nan')


def inner_length(x):
  if x is None:
    return float('nan')
  if _isFunction(x):
    return funcArgsLength(x)
  if _isFunction(getAttribute(x, 'length')):
    return number_or_nan(getAttribute(x, 'length')())
  if _has(x, 'length'):
    return number_or_nan(getAttribute(x, 'length'))
  try:
    return len(x)
  except TypeError:
    return float('nan')


length = _curry1(inner_length)
