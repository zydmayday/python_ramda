
import datetime
import unittest
from math import pi

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/constructN.js
"""


class Circle:
  def __init__(self, r, *args):
    self.r = r
    self.colors = list(args)

  def area(self):
    return self.r ** 2 * pi


class TestConstructN(unittest.TestCase):
  def test_turns_a_constructor_function_into_a_function_with_n_arguments(self):
    circle = R.constructN(2, Circle)
    c1 = circle(1, 'red')
    self.assertIsInstance(c1, Circle)
    self.assertEqual(1, c1.r)
    self.assertEqual(['red'], c1.colors)
    self.assertEqual(pi, c1.area())

  def test_can_be_used_to_create_date_object(self):
    date = R.constructN(3, datetime.date)
    d1 = date(2016)(1)(1)
    self.assertEqual(2016, d1.year)
    self.assertEqual(1, d1.month)
    self.assertEqual(1, d1.day)

  def test_supports_constructors_with_no_arguments(self):
    class Foo:
      pass
    foo = R.constructN(0, Foo)
    self.assertIsInstance(foo(), Foo)

  def test_does_not_support_constructor_with_more_than_ten_arguments(self):
    with self.assertRaises(ValueError):
      R.constructN(11, Circle)

  def test_all_arity(self):
    circle = R.constructN(1, Circle)
    self.assertEqual([], circle(1).colors)

    circle = R.constructN(2, Circle)
    self.assertEqual(['red'], circle(1)('red').colors)

    circle = R.constructN(3, Circle)
    self.assertEqual(['red', 'blue'], circle(1)('red')('blue').colors)

    circle = R.constructN(4, Circle)
    self.assertEqual(
        ['red', 'blue', 'green'],
        circle(1)('red')('blue')('green').colors)

    circle = R.constructN(5, Circle)
    self.assertEqual(
        ['red', 'blue', 'green', 'yellow'],
        circle(1)('red')('blue')('green')('yellow').colors)

    circle = R.constructN(6, Circle)
    self.assertEqual(
        ['red', 'blue', 'green', 'yellow', 'orange'],
        circle(1)('red')('blue')('green')('yellow')('orange').colors)

    circle = R.constructN(7, Circle)
    self.assertEqual(
        ['red', 'blue', 'green', 'yellow', 'orange', 'purple'],
        circle(1)('red')('blue')('green')('yellow')('orange')('purple').colors)

    circle = R.constructN(8, Circle)
    self.assertEqual(
        ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown'],
        circle(1)('red')('blue')('green')('yellow')('orange')('purple')('brown').colors)

    circle = R.constructN(9, Circle)
    self.assertEqual(
        ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'black'],
        circle(1)('red')('blue')('green')('yellow')('orange')('purple')('brown')('black').colors)

    circle = R.constructN(10, Circle)
    self.assertEqual(
        ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'black', 'white'],
        circle(1)('red')('blue')('green')('yellow')('orange')('purple')('brown')('black')('white').colors)


if __name__ == '__main__':
  unittest.main()
