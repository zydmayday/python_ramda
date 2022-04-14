def _has(obj, key):
  if isinstance(obj, dict):
    return key in obj or hasattr(obj, key)
  return hasattr(obj, key)
