from ._isArrayLike import _isArrayLike


def _has(obj, key):
  '''
  Since python object can not have None property, we just check for dict.
  '''
  if key is None:
    return isinstance(obj, dict) and key in obj
  if isinstance(obj, dict):
    try:
      return key in obj or hasattr(obj, key)
    except(TypeError):
      return False
  if _isArrayLike(obj):
    if isinstance(key, int):
      return key < len(obj)
  try:
    return hasattr(obj, key)
  except(TypeError):
    return False
