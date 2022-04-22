from .private._checkForMethod import _checkForMethod
from .private._curry3 import _curry3

slice = _curry3(_checkForMethod('slice', lambda fromIndex, toIndex, arr: arr[fromIndex:toIndex]))
