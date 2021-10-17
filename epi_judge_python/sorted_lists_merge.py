from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Time: O(n + m)
# Space: O(1)
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    curr, curr_1, curr_2 = head, L1, L2
    # While not at end of one sub array, add the smaller of curr_1 and curr_2 to the main list
    while curr_1 and curr_2:
        if curr_1.data > curr_2.data:
            curr.next = curr_2
            curr = curr.next 
            curr_2 = curr_2.next
        else:
            curr.next = curr_1
            curr = curr.next
            curr_1 = curr_1.next 
    # Add the rest of either curr_1 or curr_2
    if curr_1:
        curr.next = curr_1
    else:
        curr.next = curr_2
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
