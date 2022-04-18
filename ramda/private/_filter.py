def _filter(fn, arr):
  idx = 0
  length = len(arr)
  result = []
  while idx < length:
    if fn(arr[idx]):
      result.append(arr[idx])
    idx += 1
  return result
