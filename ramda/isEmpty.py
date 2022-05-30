from .empty import empty
from .equals import equals
from .private._curry1 import _curry1


def inner_isEmpty(x):
  return x is not None and equals(x, empty(x))


isEmpty = _curry1(inner_isEmpty)
isEmpty.__name__ = 'isEmpty'
