from .private._checkForMethod import _checkForMethod
from .private._curry1 import _curry1
from .slice import slice

tail = _curry1(_checkForMethod('tail', slice(1, None)))
