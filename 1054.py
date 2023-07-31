from collections import deque, defaultdict, Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes):
        counter = dict(Counter(barcodes))

        # 按出现次数统计元素
        sortedCounter = sorted(counter, key=lambda k: -counter[k])
        print(sortedCounter)
        barcodes = []
        # 重新排序
        for i in sortedCounter:
            barcodes += [i] * counter[i]
        print(barcodes)

        arrangedBarcodes = [None for _ in range(len(barcodes))]
        # 间隔插入
        arrangedBarcodes[::2] = barcodes[:len(arrangedBarcodes[::2])]
        arrangedBarcodes[1::2] = barcodes[len(arrangedBarcodes[::2]):]

        return arrangedBarcodes



sol = Solution()
print(sol.rearrangeBarcodes([1,1,1,2,2,2]))