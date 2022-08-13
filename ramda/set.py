from .always import always
from .over import over
from .private._curry3 import _curry3


def inner_set(lens, v, x):
  return over(lens, always(v), x)


# pylint: disable=redefined-builtin
set = _curry3(inner_set)
