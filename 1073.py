from collections import deque
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = len(arr1)
        n = len(arr2)
        res = deque()
        val = 0
        adder = 0
        if n > m:
            arr1, arr2 = arr2, arr1
            m, n = n, m
        arr2 = [0] * (m - n) + arr2

        for i in range(m - 1, -1, -1):
            if arr1[i] + arr2[i] - adder == 0:
                res.appendleft(0)
                adder = 0
            elif arr1[i] + arr2[i] - adder == 1:
                res.appendleft(1)
                val += (-2) << i
                adder = 0
            elif arr1[i] + arr2[i] - adder == 2:
                res.appendleft(0)
                val += (-2) << i
                adder = -1

        if adder != 0:
            res.appendleft(1)
            val *= 2
        return list(res)


sol = Solution()
print(sol.addNegabinary(arr1 =[1,0,1], arr2 = [1,1,1,1,1]))