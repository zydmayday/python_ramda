import pamda as R


def _arity(n, fn):
  def f0(): return fn()
  def f1(a0=R.__, *____): return fn(a0, *____)
  def f2(a0=R.__, a1=R.__, *____): return fn(a0, a1, *____)
  def f3(a0=R.__, a1=R.__, a2=R.__, *____): return fn(a0, a1, a2, *____)
  def f4(a0=R.__, a1=R.__, a2=R.__, a3=R.__, *____): return fn(a0, a1, a2, a3, *____)
  def f5(a0=R.__, a1=R.__, a2=R.__, a3=R.__, a4=R.__, *____): return fn(a0, a1, a2, a3, a4, *____)
  def f6(a0=R.__, a1=R.__, a2=R.__, a3=R.__, a4=R.__, a5=R.__, *____): return fn(a0, a1, a2, a3, a4, a5, *____)
  def f7(a0=R.__, a1=R.__, a2=R.__, a3=R.__, a4=R.__, a5=R.__, a6=R.__, *____): return fn(a0, a1, a2, a3, a4, a5, a6, *____)
  def f8(a0=R.__, a1=R.__, a2=R.__, a3=R.__, a4=R.__, a5=R.__, a6=R.__, a7=R.__, *____): return fn(a0, a1, a2, a3, a4, a5, a6, a7, *____)
  def f9(a0=R.__, a1=R.__, a2=R.__, a3=R.__, a4=R.__, a5=R.__, a6=R.__, a7=R.__, a8=R.__, *____): return fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, *____)
  def f10(a0=R.__, a1=R.__, a2=R.__, a3=R.__, a4=R.__, a5=R.__, a6=R.__, a7=R.__, a8=R.__, a9=R.__, *____): return fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, *____)
  m = {0: f0, 1: f1, 2: f2, 3: f3, 4: f4, 5: f5, 6: f6, 7: f7, 8: f8, 9: f9, 10: f10}
  if n in m:
    return m[n]
  else:
    raise Exception('First argument to _arity must be a non-negative integer no greater than ten')
