from .compose import compose
from .private._concat import _concat
from .private._curry2 import _curry2
from .uniq import uniq

union = _curry2(compose(uniq, _concat))
