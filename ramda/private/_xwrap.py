def transducer_init():
  raise ValueError('init not implemented on XWrap')


def _xwrap(fn):
  return {
      '@@transducer/init': transducer_init,
      '@@transducer/result': lambda acc: acc,
      '@@transducer/step': fn
  }
