from ._curry1 import _curry1
from ._isPlaceholder import _isPlaceholder


def _curry2(fn):
  def f2(*args):
    def f_b(_b): return fn(args[0], _b)
    if len(args) == 0:
      return f2
    if len(args) == 1:
      a = args[0]
      if _isPlaceholder(a):
        return f2

      return _curry1(f_b)
    a, b = args[0], args[1]
    if _isPlaceholder(a) and _isPlaceholder(b):
      return f2
    if _isPlaceholder(a):
      def f_a(_a): return fn(_a, b)
      return _curry1(f_a)
    if _isPlaceholder(b):
      return _curry1(f_b)
    return fn(a, b)
  return f2
