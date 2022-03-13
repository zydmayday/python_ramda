from ._arity import (_arity, ___)


def _curryN(n, saved, fn):
  def f1(*rest):
    newSaved = saved + [x for x in list(rest) if x != ___]
    newSaved = newSaved[:]
    if len(newSaved) >= n:
      return fn(*newSaved)
    else:
      return _arity(n, _curryN(n, newSaved, fn))
  return _arity(n, f1)
