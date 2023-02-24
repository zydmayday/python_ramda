from ._isArray import _isArray
from ._isInteger import _isInteger


def _assoc(prop, val, obj):
  if _isInteger(prop) and _isArray(obj):
    arr = obj[:]
    while len(arr) <= prop:
      arr.append(None)
    arr[prop] = val
    return arr
  # We have 2 cases, dict or object
  if isinstance(obj, dict):
    return {**obj, prop: val}
  raise ValueError('We only support dict or array for assoc')
