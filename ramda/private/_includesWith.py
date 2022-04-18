def _includesWith(pred, x, arr):
  idx = 0
  length = len(arr)
  while idx < length:
    if pred(x, arr[idx]):
      return True
    idx += 1
  return False
