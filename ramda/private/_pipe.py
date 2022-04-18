def _pipe(f, g):
  def inner(*arguments):
    return g(f(*arguments))
  return inner
