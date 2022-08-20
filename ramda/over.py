from .private._curry3 import _curry3


def Identity(x):
  return {'value': x, 'map': lambda f: Identity(f(x))}


def inner_over(lens, f, x):
  return lens(lambda y: Identity(f(y)))(x)['value']


over = _curry3(inner_over)
