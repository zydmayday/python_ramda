from .private._curry1 import _curry1

tail = _curry1(lambda arr: arr[1:])
