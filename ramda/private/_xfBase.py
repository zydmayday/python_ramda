from ._helper import getAttribute


class XfBase:
  """
  This is a class which not included in Ramda.
  For extracting the common part to deal with transducer related logic.
  """

  def __init__(self, xf):
    self.xf = xf

  def init(self):
    return getAttribute(self.xf, '@@transducer/init')()

  def result(self, result):
    return getAttribute(self.xf, '@@transducer/result')(result)

  def step(self, result, _input):
    pass

  def get(self, name, default=None):
    if name == '@@transducer/init':
      return self.init
    if name == '@@transducer/result':
      return self.result
    if name == '@@transducer/step':
      return self.step
    return default
