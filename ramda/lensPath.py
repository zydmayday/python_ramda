from .assocPath import assocPath
from .lens import lens
from .path import path
from .private._curry1 import _curry1


def inner_lensPath(p):
  return lens(path(p), assocPath(p))


lensPath = _curry1(inner_lensPath)
