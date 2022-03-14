from ._curry1 import _curry1
from ._curry2 import _curry2
from ._isPlaceholder import _isPlaceholder


def _curry3(fn):
  def f3(*args):
    if len(args) >= 1:
      a = args[0]
    if len(args) >= 2:
      b = args[1]
    if len(args) >= 3:
      c = args[2]

    def f_ab(_a, _b): return fn(_a, _b, c)
    def f_bc(_b, _c): return fn(a, _b, _c)
    def f_ac(_a, _c): return fn(_a, b, _c)
    def f_a(_a): return fn(_a, b, c)
    def f_b(_b): return fn(a, _b, c)
    def f_c(_c): return fn(a, b, _c)
    if len(args) == 0:
      return f3
    elif len(args) == 1:
      if _isPlaceholder(a):
        return f3
      else:
        return _curry2(f_bc)
    elif len(args) == 2:
      if _isPlaceholder(a) and _isPlaceholder(b):
        return f3
      elif _isPlaceholder(a):
        return _curry2(f_ac)
      elif _isPlaceholder(b):
        return _curry2(f_bc)
      else:
        return _curry1(f_c)
    else:
      if _isPlaceholder(a) and _isPlaceholder(b) and _isPlaceholder(c):
        return f3
      elif _isPlaceholder(a) and _isPlaceholder(b):
        return _curry2(f_ab)
      elif _isPlaceholder(a) and _isPlaceholder(c):
        return _curry2(f_ac)
      elif _isPlaceholder(b) and _isPlaceholder(c):
        return _curry2(f_bc)
      elif _isPlaceholder(a):
        return _curry1(f_a)
      elif _isPlaceholder(b):
        return _curry1(f_b)
      elif _isPlaceholder(c):
        return _curry1(f_c)
      else:
        return fn(a, b, c)
  return f3
