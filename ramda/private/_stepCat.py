from ..objOf import objOf
from ._identity import _identity
from ._isArrayLike import _isArrayLike
from ._isTransformer import _isTransformer


def _array_step(xs, x):
  return xs + [x]


_stepCatArray = {
    '@@transducer/init': list,
    '@@transducer/step': _array_step,
    '@@transducer/result': _identity
}
_stepCatString = {
    '@@transducer/init': str,
    '@@transducer/step': lambda a, b: str(a) + str(b),
    '@@transducer/result': _identity
}

_stepCatDict = {
    '@@transducer/init': dict,
    # use Python 3.9 feature
    '@@transducer/step': lambda result, input: result | (objOf(input[0], input[1]) if _isArrayLike(input) else input),
    '@@transducer/result': _identity
}

# TODO: add _stepCatObject


def _stepCat(obj):
  if _isTransformer(obj):
    return obj
  if _isArrayLike(obj):
    return _stepCatArray
  if isinstance(obj, str):
    return _stepCatString
  if isinstance(obj, dict):
    return _stepCatDict
  raise Exception(f'Cannot create transformer for {obj}')
