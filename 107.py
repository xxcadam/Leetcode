from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0] * n for _ in range(m)]
        zero_pos = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zero_pos.append((i, j))

        q = deque(zero_pos)
        seen = set(q)

        while q:
            i, j = q.popleft()
            next = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
            for x, y in next:
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    res[x][y] = res[i][j] + 1
                    q.append((x, y))
                    seen.add((x, y))

        return res


sol = Solution()
print(sol.updateMatrix([[0, 0, 0],
                        [0, 1, 0],
                        [1, 1, 1]]))