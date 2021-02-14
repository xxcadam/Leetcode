class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        res, l = 0, 0

        for r in range(0, len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)

        return res