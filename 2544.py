class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(
            int(c) if i % 2 == 0 else -int(c) for i, c in enumerate(str(n))
        )


sol = Solution()
print(sol.alternateDigitSum(886996))
