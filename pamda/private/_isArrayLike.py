from ._curry1 import _curry1


def inner_isArrayLike(x):
  return isinstance(x, (list, tuple))

_isArrayLike = _curry1(inner_isArrayLike)
