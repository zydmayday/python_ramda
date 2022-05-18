
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/reduceBy.js
"""

byType = R.prop('type')
def sumValues(acc, obj): return acc + obj['val']


sumInput = [
    {'type': 'A', 'val': 10},
    {'type': 'B', 'val': 20},
    {'type': 'A', 'val': 30},
    {'type': 'A', 'val': 40},
    {'type': 'C', 'val': 50},
    {'type': 'B', 'val': 60}
]


def grade(score):
  if score < 65:
    return 'F'
  elif score < 70:
    return 'D'
  elif score < 80:
    return 'C'
  elif score < 90:
    return 'B'
  else:
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
  return grade(student['score'] or 0)


class TestReduceBy(unittest.TestCase):
  def test_splits_the_list_into_groups_according_to_the_grouping_function(self):
    def collectNames(acc, student): return acc + [student['name']]
    self.assertEqual({
        'A': ['Dianne', 'Gillian'],
        'B': ['Abby', 'Chris', 'Irene'],
        'C': ['Brad', 'Hannah'],
        'D': ['Fred', 'Jack'],
        'F': ['Eddy']
    }, R.reduceBy(collectNames, [], byGrade, students))

  def test_splits_the_list_into_mutation_free_groups(self):
    def collectNames(acc, student):
      acc.append(student['name'])
      return acc
    self.assertEqual({
        'A': ['Dianne', 'Gillian'],
        'B': ['Abby', 'Chris', 'Irene'],
        'C': ['Brad', 'Hannah'],
        'D': ['Fred', 'Jack'],
        'F': ['Eddy']
    }, R.reduceBy(collectNames, [], byGrade, students))

  def test_returns_an_empty_object_if_given_an_empty_array(self):
    self.assertEqual({}, R.reduceBy(sumValues, 0, byType, []))

  def test_can_act_as_a_transducer(self):
    reduceToSumByType = R.reduceBy(sumValues, 0)
    sumByType = reduceToSumByType(byType)
    self.assertEqual(
        {'A': 800, 'B': 800, 'C': 500},
        R.into(
            {},
            R.compose(sumByType, R.map(R.adjust(1, R.multiply(10)))),
            sumInput)
    )

  def test_short_circuits_with_reduced(self):
    def collectNames(acc, student): return R.reduced(acc) if student['name'] == 'Fred' else acc + [student['name']]
    self.assertEqual({
        'A': ['Dianne'],
        'B': ['Abby', 'Chris'],
        'C': ['Brad'],
        'F': ['Eddy']
    }, R.reduceBy(collectNames, [], byGrade, students))
    # TODO: R.transduce


if __name__ == '__main__':
  unittest.main()
