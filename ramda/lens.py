from .map import map
from .private._curry2 import _curry2


def inner_lens(getter, setter):
  def wrapper1(toFunctorFn):
    def wrapper2(target):
      return map(lambda focus: setter(focus, target), toFunctorFn(getter(target)))
    return wrapper2
  return wrapper1


lens = _curry2(inner_lens)
