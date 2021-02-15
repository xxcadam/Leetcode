class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        result = []
        for target in range(0, length - 2):
            l = target + 1
            r = length - 1
            while l != r:
                if nums[l] + nums[r] + nums[target] == 0:
                    if [nums[target], nums[l], nums[r]] not in result:
                        result.append([nums[target], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] + nums[target] < 0:
                    l += 1
                else:
                    r -= 1
        return result
