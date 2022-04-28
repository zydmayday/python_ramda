import re

from .private._curry2 import _curry2


def inner_match(rx, s):
  return re.findall(rx, s)


match = _curry2(inner_match)
