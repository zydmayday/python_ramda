from ._curry1 import _curry1

def _curry2(fn):
  def f2(*args):
    if len(args) == 0:
      return f2
    elif len(args) == 1:
      def f3(b):
        return f2(args[0], b)
      return _curry1(f3)
    else:
      return fn(*args)
  return f2