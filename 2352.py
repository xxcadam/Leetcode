from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid2 = grid[::-1]
        print(grid)
        print(grid2)


sol = Solution()
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))