def _reduce(fn, acc, arr):
  """
  Just support list for now.
  TODO: Support full feature of reduce
  """
  if arr is None:
    return acc
  if isinstance(arr, list):
    return _arrayReduce(fn, acc, arr)
  raise Exception('reduce: list must be array or iterable')


def _arrayReduce(xf, acc, arr):
  idx = 0
  n = len(arr)
  while idx < n:
    acc = xf(acc, arr[idx])
    idx += 1
  return acc
