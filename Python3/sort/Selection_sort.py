# 时间复杂度O(n^2),空间复杂度O(1)
# 找到每个元素之后最小的，再交换

# 与冒泡排序不同点：
# 冒泡排序在比较过程中就不断交换；而选择排序增加了一个变量保存最小值 / 最大值的下标，遍历完成后才交换，减少了交换次数。
# 事实上，冒泡排序和选择排序还有一个非常重要的不同点，那就是：
# 冒泡排序法是稳定的，选择排序法是不稳定的。

# 不稳定： [2, 2, 1], 当使用冒泡排序，两个2的相对位置不发生改变，但是使用选择排序，两个2相对位置发生了改变
# 当需要排序的是跟相对顺序有关联的对象时（使用它的某个属性进行排序），就会有影响


def sort1(nums):
    for i in range(len(nums)):
        minindex = i
        for j in range(i + 1, len(nums)):
            if nums[minindex] > nums[j]:
                minindex = j
        if minindex != i:
            temp = nums[minindex]
            nums[minindex] = nums[i]
            nums[i] = temp
    return nums


# 优化，除了找出最小值，也找出最大值
def sort2(nums):
    minindex, maxindex = 0, len(nums) - 1
    i, maxindex2 = 0, maxindex
    while i < maxindex - 1:
        if nums[i] < nums[maxindex]:
            flag = 0
            maxindex2 = maxindex
            minindex = i
        else:
            flag = 1
            maxindex2 = i
            minindex = maxindex
        for j in range(i + 1, maxindex + 1):
            # if nums[j]
            if nums[j] < nums[minindex]:
                minindex = j
            elif nums[j] > nums[maxindex2]:
                maxindex2 = j
        if (flag == 0 and minindex != i) or (flag == 1 and minindex != maxindex):
            temp = nums[minindex]
            nums[minindex] = nums[i]
            nums[i] = temp
            i += 1
        if (flag == 0 and maxindex2 != maxindex) or (flag == 1 and maxindex2 != i):
            temp = nums[maxindex2]
            nums[maxindex2] = nums[maxindex]
            nums[maxindex] = temp
            maxindex -= 1
        if (flag == 0 and minindex == i and maxindex2 == maxindex) or (flag == 1 and maxindex2 == i and minindex == maxindex):
            temp = nums[maxindex2]
            nums[maxindex2] = nums[minindex]
            nums[minindex] = temp
            i += 1
            maxindex -= 1
    return nums


test = [2, 9, 1, -8, 0, 6]
print(sort2(test))
