from ._helper import getAttribute


def _xArrayReduce(xf, acc, arr):
  idx = 0
  length = len(arr)
  while idx < length:
    acc = getAttribute(xf, '@@transducer/step')(acc, arr[idx])
    if acc and getAttribute(acc, '@@transducer/reduced'):
      acc = getAttribute(acc, '@@transducer/value')
      break
    idx += 1
  return getAttribute(xf, '@@transducer/result')(acc)
