from .pipe import pipe
from .reverse import reverse


def compose(*arguments):
  if len(arguments) == 0:
    raise Exception('compose requires at least one argument')
  return pipe(*reverse(arguments))
