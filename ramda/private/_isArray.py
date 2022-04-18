def _isArray(val):
  """
  Actually array is list in Python,
  for now we do not treat tuple as an array type.
  """
  return isinstance(val, list)
