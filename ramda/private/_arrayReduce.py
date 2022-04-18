def _arrayReduce(reducer, acc, arr):
  index = 0
  length = len(arr)
  while index < length:
    acc = reducer(acc, arr[index])
    index += 1
  return acc
