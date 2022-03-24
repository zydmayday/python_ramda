from pamda.private._helper import getAttribute


def _reduced(x):
  if isinstance(x, dict) and getAttribute(x, '@@transducer/reduced'):
    return x
  else:
    return {
        {
            '@@transducer/value': x,
            '@@transducer/reduced': True
        }
    }
