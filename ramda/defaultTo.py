from .private._curry2 import _curry2

defaultTo = _curry2(lambda d, v: d if v is None else v)
