from .map import map


def join(separator, xs):
  return separator.join(map(str, xs))
