from .keys import keys
from .private._curry1 import _curry1


def static_keysIn(clazz):
  ks = [v for v, m in vars(clazz).items() if not (v.startswith('_') or callable(m))]
  for base in clazz.__bases__:
    ks += static_keysIn(base)
  return ks


def inner_keysIn(obj):
  ks = []
  primitives = (int, float, bool, str)
  # ignore primitive types
  if isinstance(obj, primitives):
    return ks
  # extract all static variables
  ks += static_keysIn(obj.__class__)
  # extract all instance variables
  ks += keys(obj)

  return ks


keysIn = _curry1(inner_keysIn)
