from .private._curry2 import _curry2


def inner_nAry(n, fn):
  if n == 0:
    return lambda *args: fn()
  if n == 1:
    return lambda a0=None, *args: fn(a0)
  if n == 2:
    return lambda a0=None, a1=None, *args: fn(a0, a1)
  if n == 3:
    return lambda a0=None, a1=None, a2=None, *args: fn(a0, a1, a2)
  if n == 4:
    return lambda a0=None, a1=None, a2=None, a3=None, *args: fn(a0, a1, a2, a3)
  if n == 5:
    return lambda a0=None, a1=None, a2=None, a3=None, a4=None, *args: fn(a0, a1, a2, a3, a4)
  if n == 6:
    return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, *args: fn(a0, a1, a2, a3, a4, a5)
  if n == 7:
    return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, *args: fn(a0, a1, a2, a3, a4, a5, a6)
  if n == 8:
    return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, a7=None, *args: fn(a0, a1, a2, a3, a4, a5, a6, a7)
  if n == 9:
    return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, a7=None, a8=None, *args: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8)
  if n == 10:
    return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, a7=None, a8=None, a9=None, *args: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
  raise ValueError('First argument to nAry must be a non-negative integer no greater than ten')


nAry = _curry2(inner_nAry)
