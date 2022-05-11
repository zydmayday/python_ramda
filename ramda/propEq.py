from .equals import equals
from .private._curry3 import _curry3
from .prop import prop


def inner_propEq(val, name, obj):
  return equals(val, prop(name, obj))


propEq = _curry3(inner_propEq)
