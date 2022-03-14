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

      def f3(b):
        return fn(args[0], b)
      return _curry1(f3)
    else:
      a, b = args[0], args[1]
      if _isPlaceholder(a) and _isPlaceholder(b):
        return f2
      elif _isPlaceholder(a):
        def f4(_a):
          return fn(_a, b)
        return _curry1(f4)
      elif _isPlaceholder(b):
        def f5(_b):
          return fn(a, _b)
        return _curry1(f5)
      return fn(a, b)
  return f2
