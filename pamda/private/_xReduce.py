from ._createReduce import _createReduce
from ._helper import getAttribute
from ._xArrayReduce import _xArrayReduce


def _xIterableReduce(xf, acc, iter):
  while True:
    try:
      acc = getAttribute(xf, '@@transducer/step')(acc, next(iter))
      if acc and getAttribute(acc, '@@transducer/reduced'):
        acc = getAttribute(acc, '@@transducer/value')
        break
    except StopIteration:
      break
  return getAttribute(xf, '@@transducer/result')(acc)


def _xMethodReduce(xf, acc, obj, methodName):
  result = getAttribute(xf, '@@transducer/result')
  method = getAttribute(obj, methodName)
  step = getAttribute(xf, '@@transducer/step')
  return result(method(step, acc))


_xReduce = _createReduce(_xArrayReduce, _xMethodReduce, _xIterableReduce)
