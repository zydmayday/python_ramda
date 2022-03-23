def _isTransformer(v):
  """
  We treat transformer as a dict in Python
  """
  return (v is not None) and (isinstance(v, dict)) and (callable(v.get('@@transducer/step')))
