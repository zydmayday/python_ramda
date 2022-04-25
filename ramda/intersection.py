from .equals import equals
from .private._curry2 import _curry2
from .private._filter import _filter
from .private._Set import _Set
from .uniq import uniq


def inner_intersection(list1, list2):
  toKeep = _Set()

  for item in list1:
    toKeep.add(item)

  # Below: change to a shorter version
  return uniq(_filter(lambda item: len([x for x in toKeep if equals(x, item)]), list2))


intersection = _curry2(inner_intersection)
