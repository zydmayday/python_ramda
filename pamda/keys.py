from pamda.private._curry1 import _curry1
from pamda.private._isFunction import _isFunction


def inner_keys(obj):
  """
  If the given obj has method keys(), just call it and return key list.
  Otherwise,
  return all attributes defined directly inside of the class, in other words, return obj.__dict__,
  if obj does not has __dict__ attribute, return empty list.

  class A:
    a = 1
    def __init__(self):
      self.b = 2
  class B(A):
    c = 3
    def __init__(self):
      self.d = 4
  b = B()
  keys(b) # ['d'], only attribute d will be included.
  """
  if hasattr(obj, 'keys') and _isFunction(obj.keys):
    return list(obj.keys())
  elif hasattr(obj, '__dict__'):
    return list(obj.__dict__)
  else:
    return []


keys = _curry1(inner_keys)