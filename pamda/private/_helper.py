from inspect import getfullargspec


def funcArgsLength(fn):
  fullargspec = getfullargspec(fn)
  return len(fullargspec.args)
