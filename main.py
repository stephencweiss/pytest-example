def increment(n):
  if not isinstance(n, int):
    raise NonIntegerException
  return n + 1

def divide(numerator, denominator):
  return numerator / denominator

class NonIntegerException(Exception):
  pass