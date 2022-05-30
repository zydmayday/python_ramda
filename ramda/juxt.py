from .converge import converge
from .private._curry1 import _curry1

juxt = _curry1(lambda fns: converge(lambda *args: list(args), fns))
juxt.__name__ = 'juxt'
