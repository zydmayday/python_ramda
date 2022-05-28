
from .curryN import curryN
from .private._curry1 import _curry1
from .private._inspect import funcArgsLength

curry = _curry1(lambda fn: curryN(funcArgsLength(fn), fn))
