class Solution:
    def findRepeatNumber(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < i:
                return nums[i]
            elif nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]

                continue
            else:
                i += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRepeatNumber(nums=[2, 3, 1, 0, 2, 5, 3]))