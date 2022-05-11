# python_ramda

This is a repo try to copy <https://github.com/ramda/ramda> in python.

## install

For whom wants to use this package.

```bash
> pip install python-ramda
> pip install python-ramda -U # get the latest
```

## Usage

```python
>>> from ramda import curry
>>> def sum(a, b, c): return a + b + c
>>> curry(sum)(1)(2, 3)
6
```

```python
>>> import ramda as R # similar to ramda syntax
>>> def sum(a, b, c): return a + b + c
>>> R.curry(sum)(1)(2, 3)
6
```

## Doc

Because the usage of `python_ramda` is almostly same to `ramda`,
so we don't create any extra doc.

If you feel any behaviour is different from what is should be in `ramda`,
please check below `CheckList` for more details.

## Contribute

For whom wants to contribute to this repo.

```bash
# see: https://pre-commit.com/ for more details
$ pre-commit install # please install hooks first
```

Checkout new branch from `main` branch directly and create PR.

## CheckList

Functions supported now.

- [x] \_\_
- [x] add

```python
  # different from ramda, ramda treat null as 0
  >>> R.add(None, None) # float('nan)
```

- [ ] addIndex
- [x] adjust
- [x] all
  - Transducer part is not fully tested.
- [ ] allPass
- [x] always
- [x] And (`and` is a keyword in python)
- [ ] andThen
- [x] any
- [ ] anyPass
- [ ] ap
- [ ] aperture
- [x] append
- [ ] apply
- [ ] applySpec
- [ ] applyTo
- [ ] ascend
- [ ] assoc
- [ ] assocPath
- [ ] binary
- [ ] bind
- [ ] both
- [ ] call
- [ ] chain
- [ ] clamp
- [x] clone

**we are simply using python `copy` module**
So with no specific reason, we suggest you to use python origin `copy` module as your first choice.

```python
class Obj:
  def __init__(self, x):
    self.value = x
obj = Obj(42)
clone = R.clone(obj)
obj == clone # False, obj and clone have different references
isinstance(clone, Obj) # True

class Obj:
  def __init__(self, x):
    self.value = x

  def __eq__(self, other):
    return self.value == other.value
obj = Obj(42)
clone = R.clone(obj)
obj == clone # True, if Obj override __eq__ function
isinstance(clone, Obj) # True
```

- [ ] collectBy
- [x] comparator
- [ ] complement
- [x] compose
- [ ] composeWith
- [x] concat
- [ ] cond
- [ ] construct
- [ ] constructN
- [ ] converge
- [ ] count
- [x] countBy
- [x] curry
- [x] curryN
- [ ] dec
- [ ] defaultTo
- [ ] descend
- [x] difference
- [x] differenceWith
- [ ] dissoc
- [ ] dissocPath
- [x] divide
- [x] drop
- [ ] dropLast
- [ ] dropLastWhile
- [ ] dropRepeats
- [ ] dropRepeatsWith
- [ ] dropWhile
- [ ] either
- [x] empty

```python
# We don't support empty object in python
class Obj:
  def __init__(self, value):
    self.value = value
o = Obj(42)
o == R.empty(o) # True, we will return the original cloned object
```

What we support for now:

1. dict()
2. set()
3. list()
4. str()
5. any instance with empty() method
6. any instance with 'fantasy-land/empty' property

- [ ] endsWith
- [ ] eqBy
- [x] eqProps

```python
# works for both dict and object
class Obj:
  def __init__(self, v):
    self.v = v
obj1 = Obj(1)
obj2 = Obj(1)
R.eqProps('v', obj1, obj2) # True
R.eqProps('v', {'v': 1}, {'v': 1}) # True
```

- [x] equals

```python
R.equals(float('nan'), float('nan')) # True
```

- [ ] evolve
- [x] F
- [x] filter
- [x] find
- [ ] findIndex
- [ ] findLast
- [ ] findLastIndex
- [x] flatten
- [x] flip
- [ ] forEach
- [ ] forEachObjIndexed
- [ ] fromPairs
- [x] groupBy
- [ ] groupWith
- [x] gt
- [x] gte
- [ ] has
- [ ] hasIn
- [ ] hasPath
- [x] head
- [ ] identical
- [x] identity
- [ ] ifElse
- [ ] inc
- [ ] includes
- [ ] indexBy
- [x] indexOf
- [ ] init
- [ ] innerJoin
- [ ] insert
- [ ] insertAll
- [x] intersection
- [ ] intersperse
- [x] into
- [ ] invert
- [ ] invertObj
- [x] invoker
- [ ] is
- [x] isEmpty

```python
class Obj:
  pass
# Any custom object will be treated as non-empty
R.isEmpty(Obj()) # False
R.isEmpty(None) # False
```

- [ ] isNil
- [x] join
- [ ] juxt
- [x] keys

```python
# When using R.keys(obj) and obj is a class instance, we use obj.__dict__ as keys.
class A:
  c = 'not included'
  def __init__(self):
    self.a = 1
    self.b = 2
a = A()
R.keys(a) # ['a', 'b']
```

- [ ] keysIn
- [ ] last
- [x] lastIndexOf
- [ ] length
- [ ] lens
- [ ] lensIndex
- [ ] lensPath
- [ ] lensProp
- [ ] lift
- [ ] liftN
- [x] lt
- [x] lte
- [x] map
- [ ] mapAccum
- [ ] mapAccumRight
- [ ] mapObjIndexed
- [x] match
- [ ] mathMod
- [x] Max (`max` is a keyword in python)

If R.Max(a, b)
`a` and `b` are with different types,
we will compare with str(a) and str(b).

```python
R.Max('A', None) # None, 'A' < 'None'
```

- [ ] maxBy
- [ ] mean
- [ ] median
- [ ] memoizeWith
- [ ] mergeAll
- [ ] mergeDeepLeft
- [ ] mergeDeepRight
- [ ] mergeDeepWith
- [ ] mergeDeepWithKey
- [ ] mergeLeft
- [ ] mergeRight
- [ ] mergeWith
- [ ] mergeWithKey
- [x] Min (`min` is a keyword in python)

If R.Min(a, b)
`a` and `b` are with different types,
we will compare with str(a) and str(b).

```python
R.Min('A', None) # 'A', 'A' < 'None'
```

- [ ] minBy
- [ ] modify
- [ ] modifyPath
- [ ] modulo
- [ ] move
- [x] multiply
- [ ] nAry
- [ ] negate
- [ ] none
- [x] not
- [x] nth
- [ ] nthArg
- [ ] o
- [x] objOf
- [ ] of
- [x] omit

we support both `dict` type and `object` type.

```python
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj = Obj(1, 2)
R.omit(['v1'], obj) # {'v2': 2}
R.omit(['v1', 'v3'], obj) # {'v2': 2}
```

- [ ] on
- [x] once
- [x] or
- [ ] otherwise
- [ ] over
- [ ] pair
- [ ] partial
- [ ] partialObject
- [ ] partialRight
- [ ] partition
- [x] path
- [ ] pathEq
- [ ] pathOr
- [x] paths
- [ ] pathSatisfies
- [x] pick
- [x] pickAll

both `pick` and `pickAll` support both `dict` and `object` type.

```python
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj = Obj(1, 2)
R.pick(['v1'], obj) # {'v1': 1}
R.pickAll(['v1', 'v3'], obj) # {'v1': 1, 'v3': None}
```

- [ ] pickBy
- [x] pipe
- [ ] pipeWith
- [x] pluck

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj1 = Obj(1, 2)
obj2 = Obj(3, 4)
R.pluck('v1', [obj1, obj2]) # [1, 3]
```

- [x] prepend
- [x] product
- [x] project

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj1 = Obj(1, 2)
obj2 = Obj(3, 4)
R.project(['v1'], [obj1, obj2]) # [{'v1': 1}, {'v1': 3}]
```

- [ ] promap
- [x] prop
- [x] propEq

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj1 = Obj(1, 2)
R.propEq(1, 'v1', obj1) # True
R.propEq(2, 'v2', obj1) # True
R.propEq(1, 'v2', obj1) # False

R.propEq(1, 'v1', {'v1': 1}) # True
```

- [ ] propIs
- [ ] propOr
- [x] props
- [ ] propSatisfies
- [x] range
- [x] reduce
- [x] reduceBy
- [x] reduced
- [ ] reduceRight
- [ ] reduceWhile
- [x] reject
- [ ] remove
- [ ] repeat
- [ ] replace
- [x] reverse
- [ ] scan
- [ ] sequence
- [ ] set
- [x] slice

```python
R.slice(1, 3, ['a', 'b', 'c', 'd']) # ['b', 'c']
R.slice(1, None, ['a', 'b', 'c', 'd']) # ['b', 'c', 'd']
```

- [x] sort
- [ ] sortBy
- [ ] sortWith
- [ ] split
- [ ] splitAt
- [ ] splitEvery
- [ ] splitWhen
- [ ] splitWhenever
- [ ] startsWith
- [ ] subtract
- [x] sum
- [ ] symmetricDifference
- [ ] symmetricDifferenceWith
- [x] T
- [x] tail
- [ ] take
- [ ] takeLast
- [ ] takeLastWhile
- [ ] takeWhile
- [ ] tap
- [ ] test
- [ ] thunkify
- [ ] times
- [ ] toLower
- [ ] toPairs
- [ ] toPairsIn
- [x] toString

Partially supported

- String type, supported
- for others, just use str(x) instead

- [ ] toUpper
- [ ] transduce
- [ ] transpose
- [ ] traverse
- [ ] trim
- [ ] tryCatch
- [ ] type
- [ ] unapply
- [ ] unary
- [ ] uncurryN
- [ ] unfold
- [ ] union
- [ ] unionWith
- [x] uniq
- [x] uniqBy
- [ ] uniqWith
- [ ] unless
- [ ] unnest
- [ ] until
- [ ] unwind
- [ ] update
- [x] useWith
- [ ] values
- [ ] valuesIn
- [ ] view
- [ ] when
- [ ] where
- [ ] whereAny
- [ ] whereEq
- [ ] without
- [ ] xor
- [ ] xprod
- [ ] zip
- [ ] zipObj
- [ ] zipWith
