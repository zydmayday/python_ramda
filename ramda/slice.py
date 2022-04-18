from .private._curry3 import _curry3

slice = _curry3(lambda fromIndex, toIndex, arr: arr[fromIndex:toIndex])
