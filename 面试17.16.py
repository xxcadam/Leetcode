from collections import deque
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)  # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]  # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1

        return max(dp0, dp1)


sol = Solution()
# print(sol.massage([1,2]))
# print(sol.massage([1,2,3,1]))
# print(sol.massage([2,7,9,3,1]))
print(sol.massage([1,2,4,5,3,1,1,3]))