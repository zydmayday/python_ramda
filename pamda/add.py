from pamda.private._curry2 import _curry2
from pamda.private._helper import toNumber

add = _curry2(lambda a, b: toNumber(a) + toNumber(b))
