from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # SLOW for testing
    # n = int(''.join([str(a) for a in A]))
    # n += 1
    # return [int(x) for x in str(n)]
    if A[-1] != 9:
        A[-1] += 1
        return A
    i = -1
    n = len(A)
    while A[i] == 9:
        # if last element is 9
        A[i] = 0
        if i == -n:
            A[0] = 1
            A.append(0)
            return A
        i -= 1
    A[i] += 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
