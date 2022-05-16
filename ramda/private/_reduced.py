from ._helper import getAttribute


def _reduced(x):
  if getAttribute(x, '@@transducer/reduced'):
    return x
  return {
      '@@transducer/value': x,
      '@@transducer/reduced': True
  }
