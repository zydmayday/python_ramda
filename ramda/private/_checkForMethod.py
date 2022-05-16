from ._helper import getAttribute
from ._isArray import _isArray
from ._isFunction import _isFunction


def _checkForMethod(methodName, fn):
  def wrapper(*arguments):
    if len(arguments) == 0:
      return fn()
    obj = arguments[-1]
    if _isArray(obj) or not _isFunction(getAttribute(obj, methodName)):
      return fn(*arguments)
    return getAttribute(obj, methodName)(*arguments[:-1])
  return wrapper
