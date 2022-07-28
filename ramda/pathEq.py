from .equals import equals
from .path import path
from .private._curry3 import _curry3

pathEq = _curry3(lambda val, _path, obj: equals(path(_path, obj), val))
