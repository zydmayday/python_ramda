import copy

from .keys import keys
from .private._curry2 import _curry2
from .private._dispatchable import _dispatchable
from .private._filter import _filter
from .private._has import _has
from .private._isArrayLike import _isArrayLike
from .private._reduce import _reduce
from .private._xfilter import _xfilter


def inner_filter(pred, filterable):
  if _isArrayLike(filterable):
    return _filter(pred, filterable)

  def inner_reduce(acc, key):
    """
    There are 2 cases of filterable
    case 1: filterable is a dict or an instance with get method
    case 2: filterable is an instance of some classes
    """
    if isinstance(filterable, dict) or _has(filterable, 'get'):
      if pred(filterable.get(key)):
        acc[key] = filterable.get(key)
    elif not pred(getattr(filterable, key, None)):
      # This is special, because we deepcopy the original object,
      # so we delete attr from original object if not match
      delattr(acc, key)
    return acc
  return _reduce(inner_reduce, {} if isinstance(filterable, dict) or _has(filterable, 'get') else copy.deepcopy(filterable), keys(filterable))


# pylint: disable=redefined-builtin
filter = _curry2(_dispatchable(['fantasy-land/filter', 'filter'], _xfilter, inner_filter))
filter.__name__ = 'filter'
