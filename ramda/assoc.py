from .assocPath import assocPath
from .private._curry3 import _curry3

assoc = _curry3(lambda prop, val, obj: assocPath([prop], val, obj))
