from ..equals import equals
from ..filter import filter


class _Set(set):
  def add(self, item):
    if filter(equals(item), list(iter(self))):
      return False
    super().add(item)
    return True
