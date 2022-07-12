from .private._curry1 import _curry1

isNil = _curry1(lambda x: x is None)
