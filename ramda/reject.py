from .filter import filter
from .private._complement import _complement
from .private._curry2 import _curry2

reject = _curry2(lambda pred, filterable: filter(_complement(pred), filterable))
reject.__name__ = 'reject'
