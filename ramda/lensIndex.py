from .lens import lens
from .nth import nth
from .private._curry1 import _curry1
from .update import update


def inner_lensIndex(n):
  return lens(nth(n), update(n))


lensIndex = _curry1(inner_lensIndex)
