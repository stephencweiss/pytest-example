def increment(n):
    if not isinstance(n, int):
        raise NonIntegerException
    return n + 1


def divide(numerator, denominator):
    if(denominator == 0):
        raise ZeroDenominator
    return numerator / denominator


class ZeroDenominator(Exception):
    pass


class NonIntegerException(Exception):
    pass
