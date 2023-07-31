class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True
        elif "abc" not in s:
            return False
        else:
            return False or self.isValid(s.replace("abc", ""))