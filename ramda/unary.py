from .nAry import nAry
from .private._curry1 import _curry1

unary = _curry1(lambda fn: nAry(1, fn))
