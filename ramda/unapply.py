from .private._curry1 import _curry1


def _unapply(func):
  def wrapper(*args):
    return func(list(args))
  return wrapper


unapply = _curry1(_unapply)
