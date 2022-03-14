def _isPlaceholder(a):
  if a is None:
    return False
  return isinstance(a, dict) and a.get('@@functional/placeholder', False)
