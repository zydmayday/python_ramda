
import unittest

import ramda as R

"""
https://github.com/ramda/ramda/blob/master/test/sortBy.js
"""

albums = [
    {'title': 'Art of the Fugue', 'artist': 'Glenn Gould', 'genre': 'Baroque'},
    {'title': 'A Farewell to Kings', 'artist': 'Rush', 'genre': 'Rock'},
    {'title': 'Timeout', 'artist': 'Dave Brubeck Quartet', 'genre': 'Jazz'},
    {'title': 'Fly By Night', 'artist': 'Rush', 'genre': 'Rock'},
    {'title': 'Goldberg Variations', 'artist': 'Daniel Barenboim', 'genre': 'Baroque'},
    {'title': 'New World Symphony', 'artist': 'Leonard Bernstein', 'genre': 'Romantic'},
    {'title': 'Romance with the Unseen', 'artist': 'Don Byron', 'genre': 'Jazz'},
    {'title': 'Somewhere In Time', 'artist': 'Iron Maiden', 'genre': 'Metal'},
    {'title': 'In Times of Desparation', 'artist': 'Danny Holt', 'genre': 'Modern'},
    {'title': 'Evita', 'artist': 'Various', 'genre': 'Broadway'},
    {'title': 'Five Leaves Left', 'artist': 'Nick Drake', 'genre': 'Folk'},
    {'title': 'The Magic Flute', 'artist': 'John Eliot Gardiner', 'genre': 'Classical'}
]


class TestSortBy(unittest.TestCase):
  def test_sorts_by_a_simple_property_of_the_objects(self):
    sortedAlbums = R.sortBy(R.prop('title'), albums)
    self.assertEqual(len(albums), len(sortedAlbums))
    self.assertEqual('A Farewell to Kings', sortedAlbums[0]['title'])
    self.assertEqual('Timeout', sortedAlbums[11]['title'])

  def test_preserves_object_identity(self):
    a = {'value': 'a'}
    b = {'value': 'b'}
    result = R.sortBy(R.prop('value'), [a, b])
    self.assertEqual(a, result[0])
    self.assertEqual(b, result[1])

  def test_sorts_array_like_object(self):
    args = (lambda *args: args)('c', 'a', 'b')
    result = R.sortBy(R.identity, args)
    self.assertEqual('a', result[0])
    self.assertEqual('b', result[1])
    self.assertEqual('c', result[2])


if __name__ == '__main__':
  unittest.main()
