from tools.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n == 0:
            return head
        result = ListNode(val=0)
        result.next = head
        temp = head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        if length == n:
            return head.next
        else:
            temp = head
            count = 0
            while count < length - n - 1:
                temp = temp.next
                count += 1
            temp = temp.next.next
            return result.next

if __name__ == '__main__':

    a = Solution()
    x = ListNode(1, ListNode(2, ListNode(3)))
    y = a.removeNthFromEnd(head=x, n=1)
    print(y.val)