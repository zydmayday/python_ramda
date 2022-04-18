def _complement(f):
  return lambda *arguments: not f(*arguments)
