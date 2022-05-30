from .private._arity import _arity
from .private._inspect import funcArgsLength
from .private._pipe import _pipe
from .reduce import reduce
from .tail import tail


def pipe(*arguments):
  if len(arguments) == 0:
    raise Exception('pipe requires at least one argument')
  return _arity(
      funcArgsLength(arguments[0]),
      reduce(_pipe, arguments[0], tail(list(arguments)))
  )
