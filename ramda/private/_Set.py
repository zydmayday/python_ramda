from math import isnan

import ramda as R

from ._isNumber import _isNumber


class _Set(set):
  def add(self, item):
    if R.filter(R.equals(item), list(self.__iter__())):
      return False
    else:
      super().add(item)
      return True
