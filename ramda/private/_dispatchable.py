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
        """
        There are 2 cases
        case1: obj is an instance of some class, that instance has method with given name
        case2: obj is a dict or an instance with get method
        """
        method = getAttribute(obj, methodNames[idx])
        if _isFunction(method):
          return method(*arguments[:-1])
        idx += 1
      if _isTransformer(obj):
        transducer = transducerCreator(*arguments[:-1])
        return transducer(obj)
    return fn(*arguments)
  return f
