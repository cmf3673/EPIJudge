from test_framework import generic_test
from test_framework.test_failure import TestFailure

# helper function for int_to_string
def int_to_char(i):
    return chr(i + ord('0'))

def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    n = abs(x)
    s = ''
    while n > 0:
        s += int_to_char(n % 10)
        n //= 10
    return ''.join(reversed(s)) if x >= 0 else '-' + ''.join(reversed(s))

# helper for string_to_int
def char_to_int(c):
    return ord(c) - ord('0')

def string_to_int(s: str) -> int:
    # n for place tracking
    sum = n = 0
    for c in reversed(s):
        if c == '-':
            return -sum
        if c == '+':
            return sum
        sum += char_to_int(c) * (10 ** n)
        n += 1
    return sum


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
