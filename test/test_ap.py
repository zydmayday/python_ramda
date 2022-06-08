
import unittest
from test.helpers.Id import Id

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/ap.js
"""

mult2 = R.multiply(2)
plus3 = R.add(3)


class TestAp(unittest.TestCase):
  def test_interprets_list_a_as_an_applicative(self):
    self.assertEqual([2, 4, 6, 4, 5, 6], R.ap([mult2, plus3])([1, 2, 3]))

  def test_interprets_arrow_r_as_an_applicative(self):
    def f(r): return lambda a: r + a
    def g(r): return r * 2
    h = R.ap(f, g)
    # (<*>) :: (r -> a -> b) -> (r -> a) -> r -> b
    # f <*> g = \x -> f x (g x)
    self.assertEqual(10 + (10 * 2), h(10))
    self.assertEqual(10 + (10 * 2), R.ap(R.add)(g)(10))

  def test_dispatches_to_the_first_passed_object_ap_method_when_values_is_a_non_array(self):
    obj = {'ap': lambda n: 'called ap with ' + str(n)}
    self.assertEqual(obj['ap'](10), R.ap(obj, 10))

  def test_works_with_fantasy_land_ap(self):
    applyX = Id(10)
    applyF = {'value': lambda x: x * 2}
    res = R.ap(applyF, applyX)
    self.assertEqual(20, res['value'])
    self.assertEqual('ramda/Id', res['@@type'])

if __name__ == '__main__':
  unittest.main()
