from .identity import identity
from .pickAll import pickAll
from .private._map import _map
from .useWith import useWith

project = useWith(_map, [pickAll, identity])
