# 冒泡排序，三种及优化，
# # 时间复杂度O(n^2),空间复杂度O(1)

# 第一种，无优化，直接冒泡排序
def sort1(nums):
    for i in range(len(nums)):
        j = 0
        while j < len(nums) - 1 - i:
            if nums[j+1] < nums[j]:
                nums[j+1] += nums[j]
                nums[j] = nums[j+1] - nums[j]
                nums[j+1] -= nums[j]
            j += 1
    return nums


# 第二种，简单优化，如果某一边没有做任何交换，则代表排序已经完成
def sort2(nums):
    for i in range(len(nums)):
        j = 0
        swapper = True
        while j < len(nums) - 1 - i:
            if nums[j + 1] < nums[j]:
                nums[j + 1] += nums[j]
                nums[j] = nums[j + 1] - nums[j]
                nums[j + 1] -= nums[j]
                swapper = False
            j += 1
        if swapper:
            break
    return nums


# 第三种，在第二种的基础上，记录上一轮最后一次交换的位置，只迭代到上一伦循环最后交换的位置
def sort3(nums):
    swapper = True
    lastSwapIndex = len(nums) - 1
    indexSwap = lastSwapIndex
    while swapper:
        i = 0
        swapper = False
        while i < lastSwapIndex:
            if nums[i+1] < nums[i]:
                nums[i+1] += nums[i]
                nums[i] = nums[i+1] - nums[i]
                nums[i+1] -= nums[i]
                swapper = True
                indexSwap = i
            i += 1
        lastSwapIndex = indexSwap
    return nums


test = [1, 5, 3, 2, 7, 4, 0]
# print(sort3(test))


#最小K个数，返回一个乱序数组最小的K个数
class Solution:
    def getLeastNumbers(self, arr, k):
        swapped = True
        LastSwapindex = len(arr) - 1
        indexSwapped = LastSwapindex

        while swapped or len(arr) - LastSwapindex - 1 <= k:
            i = 0
            swapped = False
            while i < LastSwapindex:
                if arr[i + 1] > arr[i]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    swapped = True
                    indexSwapped = i
                i += 1
            LastSwapindex = indexSwapped
        return arr[-k:]


a = Solution()
print(a.getLeastNumbers(test,2))