import collections
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        right = 0
        n = len(fruits)
        sum = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) + \
                    fruits[right][0] - fruits[left][0]

        while right < n:
            sum += fruits[right][1]
            print(f"current left, right {left, right}")
            print(f"sum, ans {sum, ans}, current step(left, right) {step(left, right)}")
            while left <= right and step(left, right) > k:
                sum -= fruits[left][1]
                left += 1

            ans = max(ans, sum)
            right += 1

        return ans


sol = Solution()
print(sol.maxTotalFruits([[200000,10000]], startPos = 0, k = 200000))



