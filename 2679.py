import math
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # res = 0
        #
        # sort_flag = False
        # while nums[0]:
        #     for i in range(len(nums)):
        #         if not sort_flag:
        #             nums[i].sort()
        #         if i == 0:
        #             maxs = nums[i].pop()
        #         else:
        #             maxs = max(nums[i].pop(), maxs)
        #     if sort_flag:
        #         sort_flag = True
        #     res += maxs
        #
        # return res
        ans = 0
        newNums = []
        for num in nums:
            newNums.append(sorted(num))
        for newnum in zip(*newNums):
            ans += max(newnum)
        return ans


sol = Solution()
print(sol.matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))