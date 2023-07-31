from typing import Optional

from ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1 or l2:
            if l1:
                num1 += str(l1.val)
                l1 = l1.next
            if l2:
                num2 += str(l2.val)
                l2 = l2.next

        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2:
            num1, num2 = num2, num1
            len1, len2 = len2, len1
        adder = 0
        tmp_node = None
        for i in range(len1):
            index1 = len1 - 1 - i
            index2 = len2 - 1 - i
            if index2 >= 0:
                tmp = int(num1[index1]) + int(num2[index2])
                val = tmp % 10
                if not tmp_node:
                    tmp_node = ListNode(val + adder)
                else:
                    tmp_node = ListNode(val + adder, tmp_node)
                adder = tmp // 10
            else:
                if not tmp_node:
                    tmp_node = ListNode(int(num1[index1]) + adder)
                else:
                    tmp_node = ListNode(int(num1[index1]) + adder, tmp_node)
                adder = 0
        while adder != 0:
            val = adder % 10
            adder = adder // 10
            tmp_node = ListNode(val, tmp_node)


        return tmp_node


sol = Solution()
print(sol.addTwoNumbers(l1=ListNode(1), l2=ListNode(9, ListNode(9))))