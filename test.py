from inspect import signature

def curry(fn):
  sig = signature(fn)
  return curryN(len(sig.parameters), fn)

def curryN(n, fn):
  return _curryN(n, [], fn)

def _curryN(n, saved, fn):
  def f1(*rest):
    newSaved = saved + list(rest)
    newSaved = newSaved[:]
    if len(newSaved) >= n:
      return fn(*newSaved)
    else:
      return _curryN(n, newSaved, fn)
  return f1

def add(a, b):
  return a + b

def multiAdd(a, b, c):
  return a + b + c

if __name__ == '__main__':
  curryAdd = curry(add)
  res = curryAdd(1)(2)
  print(res)

  curryMultiAdd = curry(multiAdd)
  print(curryMultiAdd(1)(2)(3))