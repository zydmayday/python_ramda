from ._helper import getAttribute


class XfBase:
  """
  This is a class which not included in Ramda.
  For extracting the common part to deal with transducer related logic.
  """

  def init(self):
    _init = getAttribute(self.xf, '@@transducer/init')
    if _init:
      return _init()
    return None

  def result(self, result):
    _result = getAttribute(self.xf, '@@transducer/result')
    if _result:
      return _result(result)
    return None

  def step(self, result, input):
    raise Exception('Child class should implement this')

  def get(self, name):
    if name == '@@transducer/init':
      return self.init
    if name == '@@transducer/result':
      return self.result
    if name == '@@transducer/step':
      return self.step
    return None
