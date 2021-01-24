import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        head = result
        adder = 0

        while l1 is not None and l2 is not None:
            sum1 = l1.val + l2.val + adder
            head.next = ListNode(val=sum1 % 10)
            if sum1 >= 10:
                adder = 1
            else:
                adder = 0
            l1 = l1.next
            l2 = l2.next
            head = head.next

        if l1 is not None:
            if adder is 1:
                head.next = self.addTwoNumbers(ListNode(1), l1)
            else:
                head.next = self.addTwoNumbers(ListNode(0), l1)
        elif l2 is not None:
            if adder is 1:
                head.next = self.addTwoNumbers(ListNode(1), l2)
            else:
                head.next = self.addTwoNumbers(ListNode(0), l2)
        elif adder is 1:
            head.next = ListNode(1)

        return result.next
