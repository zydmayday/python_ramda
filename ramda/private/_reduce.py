from ._arrayReduce import _arrayReduce
from ._createReduce import _createReduce
from ._helper import getAttribute
from ._xwrap import _xwrap


def _iterableReduce(reducer, acc, iter):

  while True:
    try:
      value = next(iter)
      acc = reducer(acc, value)
    except StopIteration:
      break
  return acc


def _methodReduce(reducer, acc, obj, methodName):
  method = getAttribute(obj, methodName)
  return method(reducer, acc)


_reduce = _createReduce(_arrayReduce, _methodReduce, _iterableReduce)
