from ._flatCat import _flatCat
from ._xmap import _xmap


def _xchain(f):
  return lambda xf: _xmap(f)(_flatCat(xf))
