import inspect


def _isFunction(fn):
  """
  Python class is also callable, so we need to deal with such pattern.
  class A:
    def b(self):
      return False
  a = A()
  callable(A) # True
  callable(a) # False
  callable(a.b) # True
  inspect.isclass(A) # True
  inspect.isclass(a) # False
  inspect.isclass(a.b) # False
  """
  return callable(fn) and not inspect.isclass(fn)
