from ._arrayReduce import _arrayReduce
from ._createReduce import _createReduce
from ._helper import getAttribute


def _iterableReduce(reducer, acc, _iter):

  while True:
    try:
      value = next(_iter)
      acc = reducer(acc, value)
    except StopIteration:
      break
  return acc


def _methodReduce(reducer, acc, obj, methodName):
  method = getAttribute(obj, methodName)
  return method(reducer, acc)


_reduce = _createReduce(_arrayReduce, _methodReduce, _iterableReduce)
