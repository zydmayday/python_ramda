def _forceReduced(x):
  return {
      '@@transducer/value': x,
      '@@transducer/reduced': True
  }
