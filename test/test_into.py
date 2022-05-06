import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/into.js
"""

add = R.add
def isOdd(b): return b % 2 != 0


addXf = {
    '@@transducer/step': add,
    '@@transducer/init': R.always(0),
    '@@transducer/result': R.identity
}


class TestInto(unittest.TestCase):
  def test_transduces_into_arrays(self):
    self.assertEqual([2, 3, 4, 5], R.into([], R.map(add(1)), [1, 2, 3, 4]))
    self.assertEqual([1, 3], R.into([], R.filter(isOdd), [1, 2, 3, 4]))
    # TODO: take

  def test_transduces_into_strings(self):
    self.assertEqual('2345', R.into('', R.map(add(1)), [1, 2, 3, 4]))
    self.assertEqual('13', R.into('', R.filter(isOdd), [1, 2, 3, 4]))
    # TODO: take

  def test_transduces_into_dicts(self):
    self.assertEqual({'a': 1, 'b': 2}, R.into({}, R.identity, [['a', 1], ['b', 2]]))
    self.assertEqual({'a': 1, 'b': 2, 'c': 3}, R.into({}, R.identity, [{'a': 1}, {'b': 2, 'c': 3}]))

  def test_dispatches_to_objects_that_implement_reduce(self):
    pass
    # TODO: we do not support object currently

  def test_allows_custom_transformer(self):
    intoSum = R.into(addXf)
    add2 = R.map(add(2))
    result = intoSum(add2)
    self.assertEqual(18, result([1, 2, 3, 4]))


if __name__ == '__main__':
  unittest.main()
