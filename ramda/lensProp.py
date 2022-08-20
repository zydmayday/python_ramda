from .assoc import assoc
from .lens import lens
from .private._curry1 import _curry1
from .prop import prop


def inner_lensProp(k):
  return lens(prop(k), assoc(k))


lensProp = _curry1(inner_lensProp)
