# 时间复杂度O(n^2),空间复杂度O(1)
# 从第二个开始，如果小于前面，就往前插，一直插到合适


def insertSort(nums):
    if len(nums) <= 2:
        return nums

    for i in range(len(nums) - 1):
        if nums[i+1] < nums[i]:
            current = nums[i+1]
            j = i
            while j >= 0 and nums[j] > current:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = current
    return nums

A = [1, 8, 2, 11, 3, -5, 0]
A = insertSort(A)
print(A)