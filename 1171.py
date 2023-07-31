from typing import Optional

from tools import ListNode

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        sums = []
        vals = []
        while head.next:
            if not sums:
                sums.append(head.val)
            else:
                sums.append(sums[-1] + head.val)
            vals.append(head.val)
            tmp = sums[-1]
            if tmp == 0:
                sums = []
                vals =[]
            elif tmp in sums[0:-1]:
                sums = sums[0:sums.index(tmp) + 1]
                vals = vals[0:sums.index(tmp) + 1]

            head = head.next
        res = ListNode(0)
        copy_res = res
        for val in vals:
            tmp = ListNode(val)
            copy_res.next = tmp
            copy_res = copy_res.next

        return res.next

