from .curry import curry
from .nAry import nAry
from .private._curry2 import _curry2


def inner_constructN(n, Fn):
  if n > 10:
    raise ValueError('Constructor with more than 10 arguments')
  if n == 0:
    return Fn

  def wrapper(a0, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, a7=None, a8=None, a9=None):
    if n == 1:
      return Fn(a0)
    if n == 2:
      return Fn(a0, a1)
    if n == 3:
      return Fn(a0, a1, a2)
    if n == 4:
      return Fn(a0, a1, a2, a3)
    if n == 5:
      return Fn(a0, a1, a2, a3, a4)
    if n == 6:
      return Fn(a0, a1, a2, a3, a4, a5)
    if n == 7:
      return Fn(a0, a1, a2, a3, a4, a5, a6)
    if n == 8:
      return Fn(a0, a1, a2, a3, a4, a5, a6, a7)
    if n == 9:
      return Fn(a0, a1, a2, a3, a4, a5, a6, a7, a8)
    return Fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
  return curry(nAry(n, wrapper))


constructN = _curry2(inner_constructN)
