from pamda.private._isFunction import _isFunction


def _isTransformer(v):
  """
  We treat transformer as a dict in Python
  """
  return (v is not None) and (isinstance(v, dict)) and (_isFunction(v.get('@@transducer/step')))
