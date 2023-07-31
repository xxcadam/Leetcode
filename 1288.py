from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        existing = [i for i in range(len(intervals))]
        for i in range(len(intervals)):
            if i not in existing:
                continue
            left, right = intervals[i]
            for j in range(i + 1, len(intervals)):
                if j not in existing:
                    continue
                leftc, rightc = intervals[j]
                # 如果外层被内层包含，去掉外层
                if i!=j and left >= leftc and right <= rightc:
                    del existing[existing.index(i)]
                    break
                # 如果 内层 被外层包含，去掉外层
                if i != j and left <= leftc and right >= rightc:
                    del existing[existing.index(j)]
                    continue

        print(existing)
        return len(existing)




sol = Solution()
print(sol.removeCoveredIntervals([[3, 10],[4,10],[5,11]]))