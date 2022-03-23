from ._isArray import _isArray
from ._isTransformer import _isTransformer


def _dispatchable(methodNames, transducerCreator, fn):
  def f(*arguments):
    if len(arguments) == 0:
      return fn()
    obj = arguments[-1]
    if not _isArray(obj):
      idx = 0
      while idx < len(methodNames) and isinstance(obj, dict):
        if callable(obj.get(methodNames[idx])):
          return obj.get(methodNames[idx])(*arguments[:-1])
        idx += 1
      if _isTransformer(obj):
        transducer = transducerCreator(*arguments[:-1])
        return transducer(obj)
    return fn(*arguments)
  return f
