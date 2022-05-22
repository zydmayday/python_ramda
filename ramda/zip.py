from ramda import zipWith

from .private._curry2 import _curry2
from .zipWith import zipWith

# pylint: disable=redefined-builtin
zip = _curry2(zipWith(lambda a, b: [a, b]))
