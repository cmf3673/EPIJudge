from typing import List

from test_framework import generic_test

# time complexity: O(nm)
# space complexity: O(n)
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    negative = False
    # just one negative
    if bool(num1[0] < 0) ^ bool(num2[0] < 0):
        negative = True
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    sum = 0
    n = len(num1)
    m = len(num2)
    for i in range(n):
        i_num = num1[i] * (10 ** (n - 1 - i))
        for j in range(m):
            j_num = num2[j] * (10 ** (m - 1 - j))
            sum += i_num * j_num
    sum = [int(x) for x in str(sum)]
    if negative:
        sum[0] = - sum[0]
    return sum 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
