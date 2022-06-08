import ramda as R
from ramda.private._helper import getAttribute


def Id(value):
  return {
      '@@type': 'ramda/Id',
      'fantasy-land/equals': lambda other: other is not None and getAttribute(other, '@@type') == 'ramda/Id' and R.equals(getAttribute(other, 'value'), value),
      'fantasy-land/concat': lambda id: Id(R.concat(value, getAttribute(id, 'value'))),
      'fantasy-land/map': lambda f: Id(f(value)),
      'fantasy-land/ap': lambda id: Id(getAttribute(id, 'value')(value)),
      'fantasy-land/chain': lambda f: f(value),
      'fantasy-land/reduce': lambda f, x: f(x, value),
      'fantasy-land/traverse': lambda f, of: R.map(Id, f(value)),
      'sequence': lambda of: R.map(Id, value),
      'constructor': {'fantasy-land/of': Id},
      'toString': lambda: 'Id(' + R.toString(value) + ')',
      'value': value
  }
