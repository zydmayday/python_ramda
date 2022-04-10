from ._helper import getAttribute


def _reduced(x):
  if getAttribute(x, '@@transducer/reduced'):
    return x
  else:
    return {
        '@@transducer/value': x,
        '@@transducer/reduced': True
    }
