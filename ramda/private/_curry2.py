from ..__ import __
from ._curry1 import _curry1
from ._isPlaceholder import _isPlaceholder


def _curry2(fn):
  # pylint: disable=dangerous-default-value
  # pylint: disable=keyword-arg-before-vararg
  def f2(a=__, b=__, *_):
    def f_b(_b):
      return fn(a, _b)
    if _isPlaceholder(a) and _isPlaceholder(b):
      return f2
    if _isPlaceholder(a):
      def f_a(_a):
        return fn(_a, b)
      return _curry1(f_a)
    if _isPlaceholder(b):
      return _curry1(f_b)
    return fn(a, b)
  return f2
