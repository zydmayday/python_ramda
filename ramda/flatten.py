from .private._curry1 import _curry1
from .private._makeFlat import _makeFlat

flatten = _curry1(_makeFlat(True))
