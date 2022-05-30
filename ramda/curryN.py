from .private._arity import _arity
from .private._curry2 import _curry2
from .private._curryN import _curryN

curryN = _curry2(lambda n, fn: _arity(n, _curryN(n, [], fn)))
