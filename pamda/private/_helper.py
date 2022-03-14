from inspect import getfullargspec


def funcArgsLength(fn):
  """
  Get the number of args for function fn
  Not count *args and **kwargs
  """
  fullargspec = getfullargspec(fn)
  return len(fullargspec.args)


def toNumber(a):
  """
  Convert any input a to a number type
  if can not convert, then return nan
  """
  if isinstance(a, float) or isinstance(a, int):
    return a
  try:
    return int(a)
  except:
    try:
      return float(a)
    except:
      return float('nan')
