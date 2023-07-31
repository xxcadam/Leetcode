from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        def abs_sum():
            sum = 0
            for i in range(1, len(nums)):
                sum += abs(nums[i] - nums[i - 1])
            return sum

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return abs_sum()

        orginal_sum = abs_sum()
        max_residual = 0
        for i in range(len(nums) - 1):
            if i > 0:
                left1 = abs(nums[i] - nums[i - 1])
            else:
                left1 = 0
            for j in range(i + 1, len(nums)):
                if i > 0:
                    left_residual = abs(nums[j] - nums[i - 1])
                else:
                    left_residual = 0
                if j < len(nums) - 1:
                    right_residual = abs(nums[j + 1] - nums[i]) - abs(nums[j + 1] - nums[j])
                else:
                    right_residual = 0
                if (left_residual - left1 + right_residual) > max_residual:
                    max_residual = left_residual + right_residual
                    print("Value changed for position ", i, j)
                    print(f"left, right residual is {left_residual, right_residual}")
                    print("New sum ", orginal_sum + max_residual)

        return orginal_sum + max_residual


sol = Solution()
print(sol.maxValueAfterReverse([50198,97207,3851,-96259,3530]))