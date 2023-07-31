from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        print(self.val)
        tmp = self.next
        while tmp:
            print(tmp.val)
            tmp = tmp.next

