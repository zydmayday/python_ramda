from .hasPath import hasPath
from .private._curry2 import _curry2

has = _curry2(lambda prop, obj: hasPath([prop], obj))
