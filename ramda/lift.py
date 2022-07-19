from .liftN import liftN
from .private._curry1 import _curry1
from .private._inspect import funcArgsLength

lift = _curry1(lambda fn: liftN(funcArgsLength(fn), fn))
