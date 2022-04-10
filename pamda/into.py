from .private._curry3 import _curry3
from .private._helper import getAttribute
from .private._isTransformer import _isTransformer
from .private._stepCat import _stepCat
from .private._xReduce import _xReduce


def inner_into(acc, transducer, arr):
  xf = transducer(acc if _isTransformer(acc) else _stepCat(acc))
  return _xReduce(xf, getAttribute(xf, '@@transducer/init')(), arr)


into = _curry3(inner_into)
