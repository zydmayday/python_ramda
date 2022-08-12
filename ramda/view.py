from .private._curry2 import _curry2


def Const(x):
  return {'value': x, 'fantasy-land/map': lambda *_: Const(x)}


def inner_view(lens, x):
  return lens(Const)(x)['value']


view = _curry2(inner_view)
