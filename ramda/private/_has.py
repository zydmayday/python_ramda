def _has(obj, key):
  '''
  Since python object can not have None property, we just check for dict.
  '''
  if key is None:
    return isinstance(obj, dict) and key in obj
  if isinstance(obj, dict):
    return key in obj or hasattr(obj, key)
  return hasattr(obj, key)
