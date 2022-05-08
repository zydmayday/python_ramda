from .head import head
from .paths import paths
from .private._curry2 import _curry2

path = _curry2(lambda pathAr, obj: head(paths([pathAr], obj)))
