from .adjust import adjust
from .always import always
from .private._curry3 import _curry3


def inner_update(idx, x, arr):
  return adjust(idx, always(x), arr)


update = _curry3(inner_update)
