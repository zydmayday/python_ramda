
from inspect import getfullargspec, signature

from pamda.curryN import curryN

__ = {'@@functional/playceholder': True}

# To support _arity, we need to do this tricky.
# JavaScript support arguments keyword, but no in Python
___ = {'@@functional/custome_arguments_placeholder': True}


def curry(fn):
  sig = signature(fn)
  n = len(sig.parameters)
  if getfullargspec(fn).varargs is not None:
    n -= 1
  return curryN(n, fn)
