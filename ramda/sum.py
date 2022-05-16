from .add import add
from .reduce import reduce

# pylint: disable=redefined-builtin
sum = reduce(add, 0)
