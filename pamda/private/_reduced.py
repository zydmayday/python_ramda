def _reduced(x):
  if isinstance(x, dict) and x.get('@@transducer/reduced'):
    return x
  else:
    return {
        {
            '@@transducer/value': x,
            '@@transducer/reduced': True
        }
    }
