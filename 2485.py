class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        leftsum, rightsum = (1 + n) * n // 2, n

        for i in range(n-1, 0, -1):
            if leftsum == rightsum:
                return i + 1
            if leftsum < rightsum:
                return -1
            leftsum -= i + 1
            rightsum += i
        return -1


sol = Solution()
print(sol.pivotInteger(8))