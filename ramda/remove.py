from .private._curry3 import _curry3

remove = _curry3(lambda start, count, arr: arr[:start] + arr[start + count:])
