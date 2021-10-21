from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    if start == 0 or finish == start:
        return L
    head = ListNode(None, L)
    n = 0
    i = head
    # set i to s - 1 node
    while n != start - 1:
        i = i.next
        n += 1
    prev = i.next
    curr = i.next.next
    while n != finish:
        i.next, curr.next = curr, i.next
        prev.next = curr.next
        curr = prev.next
        n += 1

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
