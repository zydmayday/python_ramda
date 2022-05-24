from ..__ import __
from ._curry1 import _curry1
from ._curry2 import _curry2
from ._isPlaceholder import _isPlaceholder


def _curry3(fn):
  # pylint: disable=dangerous-default-value
  # pylint: disable=keyword-arg-before-vararg
  def f3(a=__, b=__, c=__, *_):
    def f_ab(_a, _b): return fn(_a, _b, c)
    def f_bc(_b, _c): return fn(a, _b, _c)
    def f_ac(_a, _c): return fn(_a, b, _c)
    def f_a(_a): return fn(_a, b, c)
    def f_b(_b): return fn(a, _b, c)
    def f_c(_c): return fn(a, b, _c)
    if _isPlaceholder(a) and _isPlaceholder(b) and _isPlaceholder(c):
      return f3
    if _isPlaceholder(a) and _isPlaceholder(b):
      return _curry2(f_ab)
    if _isPlaceholder(a) and _isPlaceholder(c):
      return _curry2(f_ac)
    if _isPlaceholder(b) and _isPlaceholder(c):
      return _curry2(f_bc)
    if _isPlaceholder(a):
      return _curry1(f_a)
    if _isPlaceholder(b):
      return _curry1(f_b)
    if _isPlaceholder(c):
      return _curry1(f_c)
    return fn(a, b, c)
  return f3
