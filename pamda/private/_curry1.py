import pamda as R

from ._isPlaceholder import _isPlaceholder


def _curry1(fn):
  def f1(a = R.__, *ignored):
    if _isPlaceholder(a):
      return f1
    else:
      return fn(a)
  return f1
