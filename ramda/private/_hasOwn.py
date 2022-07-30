from ._isArrayLike import _isArrayLike


def _hasOwn(obj, prop):
  if prop is None:
    return isinstance(obj, dict) and prop in obj
  if isinstance(obj, dict):
    return prop in obj
  if _isArrayLike(obj):
    if isinstance(prop, int):
      return prop < len(obj)
  if hasattr(obj, '__dict__'):
    return prop in obj.__dict__
  return False
