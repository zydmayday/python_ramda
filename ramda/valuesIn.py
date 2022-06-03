from .keysIn import keysIn
from .private._curry1 import _curry1
from .private._helper import getAttribute

valuesIn = _curry1(lambda obj: [getAttribute(obj, key) for key in keysIn(obj)])
