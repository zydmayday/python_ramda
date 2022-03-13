# To support _arity, we need to do this tricky.
# JavaScript support arguments keyword, but no in Python
___ = {'@@functional/custome_arguments_placeholder': True}


def _arity(n, fn):
  def f0(): return fn()
  def f1(a0=___, *____): return fn(a0, *____)
  def f2(a0=___, a1=___, *____): return fn(a0, a1, *____)
  def f3(a0=___, a1=___, a2=___, *____): return fn(a0, a1, a2, *____)
  def f4(a0=___, a1=___, a2=___, a3=___, *____): return fn(a0, a1, a2, a3, *____)
  def f5(a0=___, a1=___, a2=___, a3=___, a4=___, *____): return fn(a0, a1, a2, a3, a4, *____)
  def f6(a0=___, a1=___, a2=___, a3=___, a4=___, a5=___, *____): return fn(a0, a1, a2, a3, a4, a5, *____)
  def f7(a0=___, a1=___, a2=___, a3=___, a4=___, a5=___, a6=___, *____): return fn(a0, a1, a2, a3, a4, a5, a6, *____)
  def f8(a0=___, a1=___, a2=___, a3=___, a4=___, a5=___, a6=___, a7=___, *____): return fn(a0, a1, a2, a3, a4, a5, a6, a7, *____)
  def f9(a0=___, a1=___, a2=___, a3=___, a4=___, a5=___, a6=___, a7=___, a8=___, *____): return fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, *____)
  def f10(a0=___, a1=___, a2=___, a3=___, a4=___, a5=___, a6=___, a7=___, a8=___, a9=___, *____): return fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, *____)
  m = {0: f0, 1: f1, 2: f2, 3: f3, 4: f4, 5: f5, 6: f6, 7: f7, 8: f8, 9: f9, 10: f10}
  if n in m:
    return m[n]
  else:
    raise Exception('First argument to _arity must be a non-negative integer no greater than ten')
