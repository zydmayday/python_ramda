from ._curry1 import _curry1
from ._isPlaceholder import _isPlaceholder


def _curry2(fn):
  def f2(*args):
    if len(args) == 0:
      return f2
    elif len(args) == 1:
      a = args[0]
      if _isPlaceholder(a):
        return f2

      def f_b(_b): return fn(args[0], _b)
      return _curry1(f_b)
    else:
      a, b = args[0], args[1]
      if _isPlaceholder(a) and _isPlaceholder(b):
        return f2
      elif _isPlaceholder(a):
        def f_a(_a): return fn(_a, b)
        return _curry1(f_a)
      elif _isPlaceholder(b):
        def f_b(_b): return fn(a, _b)
        return _curry1(f_b)
      return fn(a, b)
  return f2
