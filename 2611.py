from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        n = len(reward1)
        if n == 0:
            return 0
        elif k == 0:
            return sum(reward2)
        elif n == k:
            return sum(reward1)
        else:
            diff = []
            sum_reward2 = 0
            for i in range(n):
                heappush(diff, reward1[i] - reward2[i])
                sum_reward2 += reward2[i]
                if len(diff) > k:
                    heappop(diff)
                print(diff)
            while diff:
                sum_reward2 += heappop(diff)
            return sum_reward2



sol = Solution()
print(sol.miceAndCheese(reward1=[1,1,3,4], reward2=[4,4,1,1], k=2))