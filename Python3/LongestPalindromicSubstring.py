class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s

        l, r, maxlen = 0, len(s) - 1, 0
        while l + maxlen <= len(s) and r >= l:
            if s[l] == s[r]:
                x = self.count(s, l, r)
                if x != -1 and x - l + 1 > maxlen:
                    left = l
                    maxlen = x - l + 1
            if r > l:
                r -= 1
            else:
                l += 1
                r = len(s) - 1

        return s[left:left + maxlen]

    def count(self, s, l, r):
        right = r
        while s[l] == s[r] and r >= l:
            if l == r or l + 1 == r:
                return right
            l += 1
            r -= 1
        return -1