from ..__ import __
from ._isPlaceholder import _isPlaceholder


def _curry1(fn):
  # pylint: disable=dangerous-default-value
  # pylint: disable=keyword-arg-before-vararg
  def f1(a=__, *_):
    if _isPlaceholder(a):
      return f1
    return fn(a)
  return f1
