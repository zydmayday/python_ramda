def _map(fn, functor):
  idx = 0
  length = len(functor)
  result = [None] * length
  while idx < length:
    result[idx] = fn(functor[idx])
    idx += 1
  return result
