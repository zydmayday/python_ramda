from .nAry import nAry
from .private._curry1 import _curry1

binary = _curry1(lambda fn: nAry(2, fn))
