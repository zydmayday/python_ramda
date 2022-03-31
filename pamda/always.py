from .private._curry1 import _curry1


def inner_always(val):
  def f(*ignored):
    return val
  return f


always = _curry1(inner_always)
