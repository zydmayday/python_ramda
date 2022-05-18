import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/groupBy.js
"""

arr = ['foo', 'bar', 'baz', 'quux']


class TestGroupBy(unittest.TestCase):
  def test_splits_the_list_into_groups_according_to_the_grouping_function(self):
    def grade(score):
      if score < 65:
        return 'F'
      if score < 70:
        return 'D'
      if score < 80:
        return 'C'
      if score < 90:
        return 'B'
      return 'A'
    students = [
        {'name': 'Abby', 'score': 84},
        {'name': 'Brad', 'score': 73},
        {'name': 'Chris', 'score': 89},
        {'name': 'Dianne', 'score': 99},
        {'name': 'Eddy', 'score': 58},
        {'name': 'Fred', 'score': 67},
        {'name': 'Gillian', 'score': 91},
        {'name': 'Hannah', 'score': 78},
        {'name': 'Irene', 'score': 85},
        {'name': 'Jack', 'score': 69}
    ]

    def byGrade(student):
      return grade(student.get('score', 0))

    self.assertEqual({
        'A': [{'name': 'Dianne', 'score': 99}, {'name': 'Gillian', 'score': 91}],
        'B': [{'name': 'Abby', 'score': 84}, {'name': 'Chris', 'score': 89}, {'name': 'Irene', 'score': 85}],
        'C': [{'name': 'Brad', 'score': 73}, {'name': 'Hannah', 'score': 78}],
        'D': [{'name': 'Fred', 'score': 67}, {'name': 'Jack', 'score': 69}],
        'F': [{'name': 'Eddy', 'score': 58}]
    }, R.groupBy(byGrade, students))

  def test_returns_an_empty_object_if_given_an_empty_list(self):
    self.assertEqual({}, R.groupBy(R.prop('x'), []))

  def test_dispatches_on_transformer_objects_in_list_position(self):
    pass
    # TODO: R.mergeRight

  def test_can_act_as_a_transducer(self):
    def evenOdd(x):
      return 'even' if x % 2 == 0 else 'odd'
    expected = {'even': [2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}
    self.assertEqual(expected, R.into({}, R.groupBy(evenOdd), R.range(1, 10)))
    # TODO: R.transduce


if __name__ == '__main__':
  unittest.main()
