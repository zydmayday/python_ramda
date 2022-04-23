from .private._checkForMethod import _checkForMethod
from .private._curry2 import _curry2
from .reduceBy import reduceBy


def inner_groupBy(acc, item):
  acc.append(item)
  return acc


groupBy = _curry2(_checkForMethod('groupBy', reduceBy(inner_groupBy, [])))
