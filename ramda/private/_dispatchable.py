from ._helper import getAttribute
from ._isArray import _isArray
from ._isFunction import _isFunction
from ._isTransformer import _isTransformer


def _dispatchable(methodNames, transducerCreator, fn):
  def f(*arguments):
    if len(arguments) == 0:
      return fn()
    obj = arguments[-1]
    if not _isArray(obj):
      idx = 0
      while idx < len(methodNames):
        method = getAttribute(obj, methodNames[idx])
        if _isFunction(method):
          return method(*arguments[:-1])
        idx += 1
      if _isTransformer(obj):
        transducer = transducerCreator(*arguments[:-1])
        return transducer(obj)
    return fn(*arguments)
  return f
