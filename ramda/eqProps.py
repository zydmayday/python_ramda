from .equals import equals
from .private._curry3 import _curry3
from .private._helper import getAttribute


def inner_eqProps(prop, obj1, obj2):
  return equals(getAttribute(obj1, prop), getAttribute(obj2, prop))


eqProps = _curry3(inner_eqProps)
