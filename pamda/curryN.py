from pamda.private._curry1 import _curry1
from pamda.private._curry2 import _curry2
from pamda.private._curryN import _curryN

__ = {'@@functional/playceholder': True}


def inner_curryN(n, fn):
  if n == 1:
    return _curry1(fn)
  return _curryN(n, [], fn)


curryN = _curry2(inner_curryN)
