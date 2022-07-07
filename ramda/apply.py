from .private._curry2 import _curry2

apply = _curry2(lambda fn, args: fn(*args))
