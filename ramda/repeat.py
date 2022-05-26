from .always import always
from .private._curry2 import _curry2
from .times import times

repeat = _curry2(lambda value, n: times(always(value), n))
