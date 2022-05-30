from ._arity import _arity
from ._inspect import getArgsToUse
from ._isPlaceholder import _isPlaceholder


def _curryN(n, received, fn):
  def f1(*arguments):
    combined = []
    argsIdx = 0
    left = n
    combinedIdx = 0
    while combinedIdx < len(received) or argsIdx < len(arguments):
      result = None
      if combinedIdx < len(received) and ((not _isPlaceholder(received[combinedIdx])) or argsIdx >= len(arguments)):
        result = received[combinedIdx]
      else:
        result = arguments[argsIdx]
        argsIdx += 1
      combined.append(result)
      if not _isPlaceholder(result):
        left -= 1
      combinedIdx += 1
    if left <= 0:
      return fn(*getArgsToUse(fn, combined))
    return _arity(left, _curryN(n, combined, fn))
  return f1
