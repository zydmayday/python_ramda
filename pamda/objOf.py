from .private._curry2 import _curry2

"""
Since in JavaScript we can represent key-value as object,
but in Python, we can't.
So we treat objOf only works for dict in Python.
But for the naming convention, we keep the name of objOf.
"""
objOf = _curry2(lambda key, val: {key: val})
