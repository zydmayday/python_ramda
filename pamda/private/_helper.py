from inspect import getfullargspec


def funcArgsLength(fn):
  """
  Get the number of args for function fn
  Not count *args and **kwargs
  """
  fullargspec = getfullargspec(fn)
  return len(fullargspec.args)


def toNumber(a):
  """
  Convert any input a to a number type
  if can not convert, then return nan
  """
  if isinstance(a, float) or isinstance(a, int):
    return a
  try:
    return int(a)
  except:
    try:
      return float(a)
    except:
      return float('nan')

def getAttribute(v, key):
  """
  This function is mainly for retrive @@transducer/xxx property, and fantasy-land/xxx property.
  We assume dict/object in Python may own such properties.

  dict case:
    d = {'@@transducer/init': lambda: True}
    init_fn = getAttribute(d, '@@transducer/init')

  obj case:
    class T:
      def init(self):
        return True
      def get(self, type):
        if type == '@@transducer/init':
          return self.init
    t = T()
    init_fn = getAttribute(t, '@@transducer/init')

  return: function got from key, otherwise None
  """
  if isinstance(v, dict):
    if key in v:
      return v[key]
  getter = getattr(v, 'get', None)
  if getter:
    return getter(key)
  return None
