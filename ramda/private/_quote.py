import re


def _quote(s):
  s = re.sub(r'\\', r'\\\\', s)
  s = re.sub(r'[\b]', r'\\b', s)
  s = re.sub(r'\f', r'\\f', s)
  s = re.sub(r'\n', r'\\n', s)
  s = re.sub(r'\r', r'\\r', s)
  s = re.sub(r'\t', r'\\t', s)
  s = re.sub(r'\v', r'\\v', s)
  s = re.sub(r'\0', r'\\0', s)
  s = re.sub(r'"', r'\\"', s)

  return f'"{s}"'
