# pamda

This is a repo try to copy <https://github.com/ramda/ramda> in python.

## install

For whom wants to use this package.

```bash
> pip install zydmayday-pamda
> pip install zydmayday-pamda -U # get the latest
```

## Usage

```python
>>> from pamda import curry
>>> def sum(a, b, c): return a + b + c
>>> curry(sum)(1)(2, 3)
6
```

```python
>>> import pamda as R # similar to ramda syntax
>>> def sum(a, b, c): return a + b + c
>>> R.curry(sum)(1)(2, 3)
6
```

## Contribute

For whom wants to contribute to this repo.

```bash
# see: https://pre-commit.com/ for more details
$ pre-commit install # install hooks
```

Check the latest branch to be released in [here](https://github.com/zydmayday/pamda/branches).

Checkout new branch from that release branch and create PR.

## CheckList

Functions supported now.

- [x]
- [ ] add

```python
  # different from ramda, ramda treat null as 0
  >>> R.add(None, None) # float('nan)
```

- [x] __
- [x] add
- [ ] addIndex
- [ ] adjust
- [x] all
  - Transducer part is not fully tested.
- [ ] allPass
- [ ] always
- [ ] and
- [ ] andThen
- [ ] any
- [ ] anyPass
- [ ] ap
- [ ] aperture
- [ ] append
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
- [ ] clone
- [ ] collectBy
- [ ] comparator
- [ ] complement
- [x] compose
- [ ] composeWith
- [ ] concat
- [ ] cond
- [ ] construct
- [ ] constructN
- [ ] converge
- [ ] count
- [ ] countBy
- [x] curry
- [x] curryN
- [ ] dec
- [ ] defaultTo
- [ ] descend
- [ ] difference
- [ ] differenceWith
- [ ] dissoc
- [ ] dissocPath
- [ ] divide
- [ ] drop
- [ ] dropLast
- [ ] dropLastWhile
- [ ] dropRepeats
- [ ] dropRepeatsWith
- [ ] dropWhile
- [ ] either
- [ ] empty
- [ ] endsWith
- [ ] eqBy
- [ ] eqProps
- [ ] equals
- [ ] evolve
- [ ] F
- [ ] filter
- [ ] find
- [ ] findIndex
- [ ] findLast
- [ ] findLastIndex
- [ ] flatten
- [ ] flip
- [ ] forEach
- [ ] forEachObjIndexed
- [ ] fromPairs
- [ ] groupBy
- [ ] groupWith
- [ ] gt
- [ ] gte
- [ ] has
- [ ] hasIn
- [ ] hasPath
- [ ] head
- [ ] identical
- [ ] identity
- [ ] ifElse
- [ ] inc
- [ ] includes
- [ ] indexBy
- [ ] indexOf
- [ ] init
- [ ] innerJoin
- [ ] insert
- [ ] insertAll
- [ ] intersection
- [ ] intersperse
- [ ] into
- [ ] invert
- [ ] invertObj
- [ ] invoker
- [ ] is
- [ ] isEmpty
- [ ] isNil
- [ ] join
- [ ] juxt
- [ ] keys
- [ ] keysIn
- [ ] last
- [ ] lastIndexOf
- [ ] length
- [ ] lens
- [ ] lensIndex
- [ ] lensPath
- [ ] lensProp
- [ ] lift
- [ ] liftN
- [ ] lt
- [ ] lte
- [ ] map
- [ ] mapAccum
- [ ] mapAccumRight
- [ ] mapObjIndexed
- [ ] match
- [ ] mathMod
- [ ] max
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
- [ ] min
- [ ] minBy
- [ ] modify
- [ ] modifyPath
- [ ] modulo
- [ ] move
- [ ] multiply
- [ ] nAry
- [ ] negate
- [ ] none
- [ ] not
- [ ] nth
- [ ] nthArg
- [ ] o
- [ ] objOf
- [ ] of
- [ ] omit
- [ ] on
- [ ] once
- [ ] or
- [ ] otherwise
- [ ] over
- [ ] pair
- [ ] partial
- [ ] partialObject
- [ ] partialRight
- [ ] partition
- [ ] path
- [ ] pathEq
- [ ] pathOr
- [ ] paths
- [ ] pathSatisfies
- [ ] pick
- [ ] pickAll
- [ ] pickBy
- [x] pipe
- [ ] pipeWith
- [ ] pluck
- [ ] prepend
- [ ] product
- [ ] project
- [ ] promap
- [ ] prop
- [ ] propEq
- [ ] propIs
- [ ] propOr
- [ ] props
- [ ] propSatisfies
- [ ] range
- [x] reduce
- [ ] reduceBy
- [ ] reduced
- [ ] reduceRight
- [ ] reduceWhile
- [ ] reject
- [ ] remove
- [ ] repeat
- [ ] replace
- [x] reverse
- [ ] scan
- [ ] sequence
- [ ] set
- [x] slice
- [ ] sort
- [ ] sortBy
- [ ] sortWith
- [ ] split
- [ ] splitAt
- [ ] splitEvery
- [ ] splitWhen
- [ ] splitWhenever
- [ ] startsWith
- [ ] subtract
- [ ] sum
- [ ] symmetricDifference
- [ ] symmetricDifferenceWith
- [ ] T
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
- [ ] toString
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
- [ ] uniq
- [ ] uniqBy
- [ ] uniqWith
- [ ] unless
- [ ] unnest
- [ ] until
- [ ] unwind
- [ ] update
- [ ] useWith
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
