from ._has import _has
from ._isFunction import _isFunction


def _isTransformer(v):
  """
  We treat transformer as a dict in Python
  """
  return (v is not None) and (_has(v, 'get')) and (_isFunction(v.get('@@transducer/step')))
