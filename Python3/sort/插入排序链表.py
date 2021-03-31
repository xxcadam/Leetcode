from tools.ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        res = ListNode()
        res.next = head

        while head.next is not None:
            if head.next.val < head.val:
                tmp = res
                current = head.next.val
                head.next = head.next.next
                while tmp.next.val < current:
                    tmp = tmp.next
                tmp.next = ListNode(current, tmp.next)

        return res.next
