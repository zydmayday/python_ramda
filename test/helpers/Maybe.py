import ramda as R
from ramda.private._helper import getAttribute

sentinel = {}


class Maybe:
  def __init__(self, x, box):
    if x != sentinel:
      raise Exception('Can not instantiate Maybe')
    self.isJust = len(box) > 0
    if self.isJust:
      self.value = box[0]
    self.isNothing = not self.isJust

  def equals(self, other):
    if other is not None and getAttribute(other, '@@type') == getAttribute(self, '@@type') and self.isJust:
      return other.isJust and R.equals(self.value, other.value)
    else:
      return other.isNothing

  def map(self, f):
    if self.isJust:
      return Just(f(self.value))
    else:
      return Nothing()

  def ap(self, maybe):
    if self.isJust and getAttribute(maybe, 'isJust'):
      return Just(maybe.value(self.value))
    else:
      return Nothing()

  def chain(self, f):
    if self.isJust:
      return f(self.value)
    else:
      return Nothing()

  def filter(self, pred):
    if self.isJust and pred(self.value):
      return self
    else:
      return Nothing()

  def toSring(self):
    if self.isJust:
      return 'Just(' + R.toString(self.value) + ')'
    else:
      return 'Nothing'

  def empty(self):
    return Nothing()

  def get(self, name, default=None):
    if name == 'fantasy-land/of':
      return Just
    if name == '@@type':
      return 'ramda/Maybe'
    if name == 'fantasy-land/equals':
      return self.equals
    if name == 'fantasy-land/map':
      return self.map
    if name == 'fantasy-land/ap':
      return self.ap
    if name == 'fantasy-land/chain':
      return self.chain
    if name == 'fantasy-land/filter':
      return self.filter
    if name == 'fantasy-land/empty':
      return self.empty
    return default


class Nothing(Maybe):
  def __init__(self, value=[]):
    super().__init__(sentinel, value)


class Just(Maybe):
  def __init__(self, value):
    super().__init__(sentinel, [value])
