from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        if not head:
            return res

        while head.next:
            res.append(head.val)
            head = head.next
        res.append(head.val)
        return res[::-1]

