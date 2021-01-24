class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if nums[i] not in dic.keys():
                dic[diff] = i
            else:
                return [dic[nums[i]], i]