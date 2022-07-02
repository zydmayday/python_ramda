from .defaultTo import defaultTo
from .private._curry3 import _curry3
from .prop import prop

propOr = _curry3(lambda val, p, obj: defaultTo(val, prop(p, obj)))
