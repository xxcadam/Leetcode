class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # 1 10 11 100 101 111 10000
        for i in range(1, n + 1):
            j = bin(i)
            if j[2:] not in s:
                return False
        return True


sol = Solution()
sol.queryString("0100", 8)