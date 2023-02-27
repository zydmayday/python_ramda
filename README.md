# python_ramda

This is a repo try to copy <https://github.com/ramda/ramda> in python.

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
![PyPI version](https://badge.fury.io/py/python-ramda.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/python-ramda.svg)
[![codecov](https://codecov.io/gh/zydmayday/python_ramda/branch/main/graph/badge.svg?token=2AHXPONAYV)](https://codecov.io/gh/zydmayday/python_ramda)

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
$ pip install -U pylint
# see: https://pre-commit.com/ for more details
$ pre-commit install # please install hooks first
```

Checkout new branch from `main` branch directly and create PR.

## CheckList

Functions supported now.

- [x] 0.1.2 \_\_
- [x] 0.1.2 add

```python
# different from ramda
R.add(None, None) # float('nan)
R.add(date(1,2,3), date(1,2,3)) # float('nan)
```

- [ ] addIndex
- [x] 0.1.2 adjust
- [x] 0.1.2 all
  - Transducer part is not fully tested.
- [ ] allPass
- [x] 0.1.2 always
- [x] 0.1.2 And (`and` is a keyword in python)
- [ ] andThen
- [x] 0.1.2 any
- [ ] anyPass
- [x] 0.3.0 ap
- [ ] aperture
- [x] 0.1.2 append
- [x] 0.7.0 apply
- [ ] applySpec
- [ ] applyTo
- [ ] ascend
- [x] 0.8.0 assoc

Currently, we only support list and dict type.

- [x] 0.8.0 assocPath

Currently, we only support list and dict type.

- [x] 0.2.0 binary
- [ ] bind
- [ ] both
- [ ] call
- [x] 0.3.0 chain
- [ ] clamp
- [x] 0.1.2 clone

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
- [x] 0.1.2 comparator
- [ ] complement
- [x] 0.1.2 compose
- [ ] composeWith
- [x] 0.1.2 concat
- [x] 0.6.0 cond

Please notice the number of given arguments should match functions.
Otherwise Python will complain about the mis-matching arguments.

For example:

```python
fn = R.cond([
  [lambda a: a == 1, lambda a: f'a == {a}'],
  [lambda a, b: a == b, lambda a, b: f'{a} == {b}']
])
fn(1) # a == 1
fn(2, 2) # 2 == 2

fn(2) # Throw error, because b is not provided for prediction, failed when (lambda a, b: a == b)(2), missing argument b
# to solve above issue, you should try your best to provide enough arguments

fn(1, 2) # Throw error, because (lambda(a: f'a == {a}'))(1, 2) has extra arguments 2
# To solve above issue, always use sencond function with enough arguments
# Try create cond like below.
fn = R.cond([
  [lambda a: a == 1, lambda a, _: f'a == {a}'], # ignore b
  [lambda a, b: a == b, lambda a, b: f'{a} == {b}']
])

fn = R.cond([
  [lambda a: a == 1, lambda a, *args: f'a == {a}'], # ignore any arguments
  [lambda a, b: a == b, lambda a, b: f'{a} == {b}']
])
```

- [x] 0.4.0 construct
- [x] 0.4.0 constructN
- [x] 0.1.4 converge
- [ ] count
- [x] 0.1.2 countBy
- [x] 0.1.2 curry
- [x] 0.1.2 curryN
- [ ] dec
- [x] 0.6.0 defaultTo
- [ ] descend
- [x] 0.1.2 difference
- [x] 0.1.2 differenceWith
- [ ] dissoc
- [ ] dissocPath
- [x] 0.1.2 divide
- [x] 0.1.2 drop
- [ ] dropLast
- [ ] dropLastWhile
- [ ] dropRepeats
- [ ] dropRepeatsWith
- [ ] dropWhile
- [ ] either
- [x] 0.1.2 empty

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
- [x] 0.1.2 eqProps

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

- [x] 0.1.2 equals

```python
R.equals(float('nan'), float('nan')) # True
```

- [ ] evolve
- [x] 0.1.2 F
- [x] 0.1.2 filter
- [x] 0.1.2 find
- [x] 0.1.4 findIndex
- [x] 0.1.4 findLast
- [x] 0.1.4 findLastIndex
- [x] 0.1.2 flatten
- [x] 0.1.2 flip
- [x] 0.1.4 forEach
- [ ] forEachObjIndexed
- [x] 0.3.0 fromPairs
- [x] 0.1.2 groupBy
- [ ] groupWith
- [x] 0.1.2 gt
- [x] 0.1.2 gte
- [x] 0.7.0 has

Similar to `hasPath`.

- [x] 0.7.0 hasIn

works for both dict and object

```python
class Obj:
  def __init__(self, v):
    self.v = v

obj1 = Obj(1)
R.hasIn('v', obj1) # True
R.hasIn('v', {'v': 1}) # True
```

- [x] hasPath
Support both dict and object.

```python

R.hasPath(['a', 'b'], {'a': {'b': 42}}) # True

class Obj:
  def __init__(self, v):
    self.v = v
obj = Obj(1)

R.hasPath(['v'], obj) # True
R.hasPath(['v', 'child'], obj) # False

R.hasPath(['v'], {'v': 1}) # True
R.hasPath(['v', 'child'], {'v': 1}) # False

# Does not include static variable
class Obj:
  v = 1
obj = Obj()
R.hasPath(['v'], obj) # False

# Also support inherited variable
class Parent:
  def __init__(self, a):
    self.a = a
class Child(Parent):
  def __init__(self, a,b):
    super().__init__(a)
    self.b = b
child = Child(1, 2)
R.hasPath(['a'], child) # True
R.hasPath(['b'], child) # True
```

- [x] 0.1.2 head
- [ ] identical
- [x] 0.1.2 identity
- [x] 0.8.0 ifElse
- [x] inc
- [ ] includes
- [ ] indexBy
- [x] 0.1.2 indexOf
- [ ] init
- [ ] innerJoin
- [x] 0.2.2 insert
- [ ] insertAll
- [x] 0.1.2 intersection
- [ ] intersperse
- [x] 0.1.2 into
- [ ] invert
- [ ] invertObj
- [x] 0.1.2 invoker
- [x] 0.3.0 Is (`is` is a keyword in python)

This is a language specific feature.
So we check all python built-in types as many as we can.

```python
R.Is(int, 1) # True
R.Is(float, 1.0) # True
R.Is(str, '1') # True
R.Is(list, [1,2,3]) # True
R.Is(dict, {'a': 1}) # True
R.Is(set, {1,2,3}) # True
R.Is(tuple, (1,2,3)) # True
R.Is(None, None) # True
R.Is(bool, True) # True
R.Is(bool, False) # True

# For user-defined object
class Parent:
  pass
class Child(Parent):
  pass
R.Is(Parent, Parent()) # True
R.Is(Parent, Child()) # True
R.Is(Child, Child()) # True
R.Is(Child, Parent()) # False
````

- [x] 0.1.2 isEmpty

```python
class Obj:
  pass
# Any custom object will be treated as non-empty
R.isEmpty(Obj()) # False
R.isEmpty(None) # False
```

- [x] isNil

We keep the same method name as ramda,
this is for checking if the given value is None or not.

- [x] 0.1.2 join
- [x] 0.1.4 juxt
- [x] 0.1.2 keys

For object, `keys` does not return object's methods.

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

```python
# keys include super class attributes
class A:
  def __init__(self, a):
    self.a = a

class B(A):
  def __init__(self, a, b):
    super().__init__(a)
    self.b = b

class C(A):
  def __init__(self, c):
    self.c = c

a = A(1)
b = B(2, 3)
c = C(4)
R.keys(a) # ['a']
R.keys(b) # ['a', 'b']
R.keys(c) # ['c'], because c does not call super().__init__()

# For normal dict
R.keys({'a': 1, 'b': 2}) # ['a', 'b']
```

- [x] 0.2.0 keysIn

For object, `keysIn` does not return object's methods.

Different from `keys`, `keysIn` will return all attributes of the object, including super class attributes and class static variables.

```python
class A:
  a_static = 1
  def __init__(self):
    self.a = 1
class B(A):
  b_static = 2
  def __init__(self, b):
    super().__init__()
    self.b = b

R.keysIn(A()) # ['a_static', 'a']
R.keysIn(B(2)) # ['a_static', 'a', 'b_static', 'b']

# For normal dict
R.keysIn({'a': 1, 'b': 2}) # ['a', 'b']
```

- [x] 0.1.4 last
- [x] 0.1.2 lastIndexOf
- [x] 0.3.0 length

The behavior of `length` is different from `ramda`.

```python
# Array
R.length([1, 2, 3]) # 3
# String
R.length('abc') # 3
# Dict
R.length({'a': 1, 'b': 2}) # 2
# Set
R.length({1, 2, 3}) # 3
# Tuple
R.length((1, 2, 3)) # 3
# Notice: Also works for any other iterable object

# Some special cases
# object with length() method
class Obj:
  def length(self):
    return 3
obj = Obj()
R.length(obj) # 3

# dict with length property
R.length({'a': 1, 'length': 99}) # 99, R.length will use length property instead

# return function arguments length
def f(a, b, c):
  return a + b + c
R.length(f) # 3

# Any failed cases, return nan instead
R.length(None) # float('nan')
R.length(1) # float('nan')
class ObjWithoutLength:
  pass
R.length(ObjWithoutLength()) # float('nan')
```

- [x] 0.8.0 lens
- [x] lensIndex
- [x] lensPath
- [x] lensProp
- [x] 0.7.0 lift
- [x] 0.7.0 liftN
- [x] 0.1.2 lt
- [x] 0.1.2 lte
- [x] 0.1.2 map
- [ ] mapAccum
- [ ] mapAccumRight
- [ ] mapObjIndexed
- [x] 0.1.2 match
- [x] 0.3.0 mathMod
- [x] 0.1.2 Max (`max` is a keyword in python)

If R.Max(a, b)
`a` and `b` are with different types,
we will compare with str(a) and str(b).

```python
R.Max('A', None) # None, 'A' < 'None'
```

- [x] 0.8.0 maxBy
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
- [x] 0.1.2 Min (`min` is a keyword in python)

If R.Min(a, b)
`a` and `b` are with different types,
we will compare with str(a) and str(b).

```python
R.Min('A', None) # 'A', 'A' < 'None'
```

- [x] 0.8.0 minBy
- [ ] modify
- [ ] modifyPath
- [x] 0.1.4 modulo

Python modulo on negative numbers has different behavior than JS.

```python
5 % -3 # -1
```

```js
5 % -3; // 2
```

- [ ] move
- [x] 0.1.2 multiply
- [x] 0.2.0 nAry
- [ ] negate
- [ ] none
- [x] 0.1.2 not
- [x] 0.1.2 nth
- [ ] nthArg
- [ ] o
- [x] 0.1.2 objOf
- [x] 0.3.0 of
- [x] 0.1.2 omit

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
- [x] 0.1.2 once
- [x] 0.1.2 or
- [ ] otherwise
- [x] over
- [ ] pair
- [ ] partial
- [ ] partialObject
- [ ] partialRight
- [x] 0.1.4 partition
- [x] 0.1.2 path
- [x] 0.7.0 pathEq
- [ ] pathOr
- [x] 0.1.2 paths
- [ ] pathSatisfies
- [x] 0.1.2 pick
- [x] 0.1.2 pickAll

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

- [x] 0.8.0 pickBy
- [x] 0.1.2 pipe
- [ ] pipeWith
- [x] 0.1.2 pluck

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

- [x] 0.1.2 prepend
- [x] 0.1.2 product
- [x] 0.1.2 project

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
- [x] 0.1.2 prop
- [x] 0.1.2 propEq

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
- [x] 0.6.0 propOr
- [x] 0.1.2 props
- [ ] propSatisfies
- [x] 0.1.2 range
- [x] 0.1.2 reduce
- [x] 0.1.2 reduceBy
- [x] 0.1.2 reduced
- [x] 0.1.2 reduceRight
- [ ] reduceWhile
- [x] 0.1.2 reject
- [x] 0.2.2 remove
- [x] 0.1.4 repeat
- [x] 0.7.0 replace
- [x] 0.1.2 reverse
- [ ] scan
- [ ] sequence
- [x] set
- [x] 0.1.2 slice

```python
R.slice(1, 3, ['a', 'b', 'c', 'd']) # ['b', 'c']
R.slice(1, None, ['a', 'b', 'c', 'd']) # ['b', 'c', 'd']
```

- [x] 0.1.2 sort
- [x] 0.1.2 sortBy
- [ ] sortWith
- [x] 0.1.2 split
- [ ] splitAt
- [ ] splitEvery
- [ ] splitWhen
- [ ] splitWhenever
- [ ] startsWith
- [x] 0.1.2 subtract

```python
# different from ramda
R.subtract(None, None) # float('nan)
R.subtract(date(1,2,3), date(1,2,3)) # float('nan)
```

- [x] 0.1.2 sum
- [ ] symmetricDifference
- [ ] symmetricDifferenceWith
- [x] 0.1.2 T
- [x] 0.1.2 tail
- [x] 0.1.2 take
- [ ] takeLast
- [ ] takeLastWhile
- [x] 0.1.2 takeWhile
- [x] 0.1.2 tap
- [ ] test
- [ ] thunkify
- [x] 0.1.4 times
- [ ] toLower
- [x] 0.4.0 toPairs

```python
R.toPairs({'a': 1, 'b': 2}) # [['a', 1], ['b', 2]]

class A:
  v1 = 'not included'
  def __init__(self, v2):
    self.v2 = v2

R.toPairs(A(1)) # [['v2', 1]]

class B(A):
  v3 = 'not included'
  def __init__(self, v2, v4):
    super().__init__(v2) # this is required
    self.v4 = v4

b = B('v2', 'v4')
R.toPairs(b) # [['v2', 'v2'], ['v4', 'v4']]
```

- [x] 0.4.0 toPairsIn

```python
R.toPairsIn({'a': 1, 'b': 2}) # [['a', 1], ['b', 2]]

class A:
  v1 = 'included'
  def __init__(self, v2):
    self.v2 = v2

R.toPairsIn(A('v2')) # [['v1', 'included'], ['v2', 'v2']]

class B(A):
  v3 = 'included too'
  def __init__(self, v2, v4):
    super().__init__(v2) # this is required
    self.v4 = v4

R.toPairsIn(B('v2', 'v4')) # [['v3', 'included too'], ['v1', 'included'], ['v2', 'v2'], ['v4', 'v4']]
```

- [x] 0.1.2 toString

Partially supported

1. String type, supported
1. for others, just use str(x) instead

- [x] toUpper
- [ ] transduce
- [ ] transpose
- [ ] traverse
- [x] 0.6.0 trim
- [ ] tryCatch
- [ ] type
- [x] 0.8.0 unapply
- [x] 0.2.0 unary
- [ ] uncurryN
- [ ] unfold
- [x] 0.1.2 union
- [x] 0.1.2 unionWith
- [x] 0.1.2 uniq
- [x] 0.1.2 uniqBy
- [x] 0.1.2 uniqWith
- [ ] unless
- [x] 0.3.0 unnest
- [ ] until
- [ ] unwind
- [x] update
- [x] 0.1.2 useWith
- [x] 0.1.2 values

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj = Obj(1, 2)
R.values(obj) # [1, 2]
R.values({'a': 1, 'b': 2}) # [1, 2]
```

- [x] 0.2.0 valuesIn

Use `R.keysIn` to get the keys of an object.

- [x] view
- [ ] when
- [x] 0.1.4 where

spec(first param) is prefer to be a dict.

method `where` supports both dict and object as second param.

```python
class Obj:
  def __init__(self, x, y):
    self.x = x
    self.y = y

spec = {'x': R.equals(1)}
R.where(spec, {'x': 1, 'y': 2}) # True
R.where(spec, Obj(1, 2)) # True
```

- [ ] whereAny
- [ ] whereEq
- [ ] without
- [ ] xor
- [x] 0.1.2 xprod
- [x] 0.1.2 zip
- [x] 0.3.0 zipObj

It will return a dict.

- [x] 0.1.2 zipWith
