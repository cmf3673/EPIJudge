from test_framework import generic_test

# base b1 to base 10
def to_ten(s, b1):
    sum = n = 0
    for c in reversed(s):
        if c == '-':
            return -sum
        i = int(c) if c.isdigit() else ord(c) - 55
        sum += i * b1 ** n
        n += 1
    return sum

# base 10 to base b2
def to_b2(n, b2):
    if not n:
        return '0'
    k = abs(n)
    s = ''
    while k > 0:
        i = str(k % b2) if not k % b2 // 10 else chr(k % b2 + 55)
        s += i
        k //= b2
    return ''.join(reversed(s)) if n > 0 else '-' + ''.join(reversed(s))

# Time: O(n)
# Space: O(n)
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    b10 = to_ten(num_as_string, b1) if b1 != 10 else int(num_as_string)
    return to_b2(b10, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
