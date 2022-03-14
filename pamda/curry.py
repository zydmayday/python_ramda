
from pamda.curryN import curryN
from pamda.private._curry1 import _curry1
from pamda.private._helper import funcArgsLength

curry = _curry1(lambda fn: curryN(funcArgsLength(fn), fn))
