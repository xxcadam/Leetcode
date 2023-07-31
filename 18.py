from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            j = i + 1
            while j < len(nums) - 2:
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    foursum = nums[i] + nums[j] + nums[k] + nums[l]
                    if foursum > target:
                        l -= 1
                        continue
                    elif foursum < target:
                        k += 1
                        continue
                    else:
                        a = [nums[i], nums[j], nums[k], nums[l]]
                        if a not in res:
                            res.append(a)
                        k += 1
                j += 1
        return res

