from math import inf
from typing import List

from test_framework import generic_test

# Time: O(n)
# Space: O(1)
def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_p = float('-inf')
    max_d = float('-inf')
    for p in prices[::-1]:
        if p > max_p: max_p = p
        if max_p - p > max_d: max_d = max_p - p
    return max_d


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
