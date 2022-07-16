
import math

from ._has import _has
from ._isArrayLike import _isArrayLike
from ._isInteger import _isInteger
from ._isNumber import _isNumber


def toNumber(a):
  """
  Convert any input a to a number type
  if can not convert, then return nan
  """
  if _isNumber(a):
    return a
  try:
    return int(a)
  except (ValueError, TypeError):
    try:
      return float(a)
    except (ValueError, TypeError):
      return float('nan')


# pylint: disable=inconsistent-return-statements
def getAttribute(v, key):
  """
  This function is mainly for retrive @@transducer/xxx property, and fantasy-land/xxx property.
  We assume dict/object in Python may own such properties.

  dict case:
    d = {'@@transducer/init': lambda: True}
    init_fn = getAttribute(d, '@@transducer/init')

  obj case:
    class T:
      def init(self):
        return True
      def get(self, type):
        if type == '@@transducer/init':
          return self.init
    t = T()
    init_fn = getAttribute(t, '@@transducer/init')

  method case 1:
    class Mapper:
      def map(fn):
        return fn
    m = Mapper()
    map_fn = getAttribute(m, 'map')

  method case 2:
    class Mapper:
      def map(self, fn):
        return fn
    m = Mapper()
    map_fn = getAttribute(m, 'map')

  return: function got from key, otherwise None
  """
  if isinstance(v, dict) and key in v:
    return v[key]
  if _isArrayLike(v) and _isInteger(key):
    return v[key]
  if _has(v, key):
    return getattr(v, key, None)
  if _has(v, 'get'):
    try:
      # Case that get is (key, default) -> value signature
      return v.get(key, default=None)
    except TypeError:
      try:
        # Case that get is a instance method with (self, key, default) -> value signature
        return v.get(v, key, default=None)
      except TypeError:
        # Unknown signature
        return None


def safeLen(x):
  if _isArrayLike(x):
    return len(x)
  return 0


def isNegativeFloatZero(n):
  return n == 0 and math.atan2(0.0, 0.0) != math.atan2(0.0, n)
