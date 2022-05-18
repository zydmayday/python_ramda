from .private._concat import _concat
from .private._curry3 import _curry3
from .uniqWith import uniqWith

unionWith = _curry3(lambda pred, list1, list2: uniqWith(pred, _concat(list1, list2)))
