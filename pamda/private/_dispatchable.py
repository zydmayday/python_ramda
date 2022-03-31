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
        methodName = methodNames[idx]
        """
        There are 2 cases
        case1: obj is an instance of some class, that instance has method with given name
        case2: obj is a dict or an instance with get method
        """

        # case 1
        if hasattr(obj, methodName):
          method = getattr(obj, methodName, None)
          if _isFunction(method):
            return method(*arguments[:-1])
        # case 2
        if isinstance(obj, dict) or hasattr(obj, 'get'):
          if _isFunction(obj.get(methodName)):
            return obj.get(methodName)(*arguments[:-1])
        idx += 1
      if _isTransformer(obj):
        transducer = transducerCreator(*arguments[:-1])
        return transducer(obj)
    return fn(*arguments)
  return f
