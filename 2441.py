from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dpossible = set()
        res = -1
        for i in nums:
            if -i in dpossible:
                if abs(i) > res:
                    res = abs(i)
            else:
                dpossible.add(i)
        return res

