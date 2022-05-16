import copy


def _clone(value, deep=True):
  """
  Unless there is no problem, we will use the built-in copy module.
  """
  if deep:
    return copy.deepcopy(value)
  return copy.copy(value)
