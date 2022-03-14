from pamda.private._arity import _arity
from pamda.private._curry1 import _curry1
from pamda.private._curry2 import _curry2
from pamda.private._curryN import _curryN


def _inner_curryN(n, fn):
  if n == 1:
    return _curry1(fn)
  return _arity(n, _curryN(n, [], fn))


curryN = _curry2(_inner_curryN)
