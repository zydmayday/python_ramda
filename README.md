# pamda

This is a repo try to copy https://github.com/ramda/ramda in python.

## install

```bash
$ pip install zydmayday-pamda
$ pip install zydmayday-pamda -U # get the latest
```

## Usage

```python
>>> from pamda import curry
>>> def add(a,b,c): return a + b + c
...
>>> curry(add)(1)(2,3)
6
```
