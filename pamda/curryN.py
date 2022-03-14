from pamda.private._arity import _arity
from pamda.private._curry1 import _curry1
from pamda.private._curry2 import _curry2
from pamda.private._curryN import _curryN

curryN = _curry2(lambda n, fn: _curry1(fn) if n == 1 else _arity(n, _curryN(n, [], fn)))
