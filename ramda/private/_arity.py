from ..__ import __


# pylint: disable=dangerous-default-value
# pylint: disable=keyword-arg-before-vararg
def _arity(n, fn):
  def f0(*_): return fn(*_)
  def f1(a0=__, *_): return fn(a0, *_)
  def f2(a0=__, a1=__, *_): return fn(a0, a1, *_)
  def f3(a0=__, a1=__, a2=__, *_): return fn(a0, a1, a2, *_)
  def f4(a0=__, a1=__, a2=__, a3=__, *_): return fn(a0, a1, a2, a3, *_)
  def f5(a0=__, a1=__, a2=__, a3=__, a4=__, *_): return fn(a0, a1, a2, a3, a4, *_)
  def f6(a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, *_): return fn(a0, a1, a2, a3, a4, a5, *_)
  def f7(a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, *_): return fn(a0, a1, a2, a3, a4, a5, a6, *_)
  def f8(a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, a7=__, *_): return fn(a0, a1, a2, a3, a4, a5, a6, a7, *_)
  def f9(a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, a7=__, a8=__, *_): return fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, *_)
  def f10(a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, a7=__, a8=__, a9=__, *_): return fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, *_)
  m = {0: f0, 1: f1, 2: f2, 3: f3, 4: f4, 5: f5, 6: f6, 7: f7, 8: f8, 9: f9, 10: f10}
  if n in m:
    return m[n]
  raise Exception('First argument to _arity must be a non-negative integer no greater than ten')
