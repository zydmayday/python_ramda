class X:
  """
  This is a class which not included in Ramda.
  For extracting the common part to deal with transducer related logic.
  """

  def init(self):
    raise Exception('Child class should implement this')

  def result(self, result):
    raise Exception('Child class should implement this')

  def step(self, result, input):
    raise Exception('Child class should implement this')

  def get(self, name):
    if name == '@@transducer/init':
      return self.init
    if name == '@@transducer/result':
      return self.result
    if name == '@@transducer/step':
      return self.step
    raise Exception('Undefined transducer name, please provide one of the following: [@@transducer/init, @@transducer/result, @@transducer/step]')
