from collections import Counter
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:

        l = len(words)
        res = 0
        for i in range(l - 1):
            le = len(words[i])
            x_counter = Counter(words[i])
            max_re = 0
            for j in range(1, l):
                re = len(words[j])
                if re < max_re:
                    continue
                y_counter = Counter(words[j])
                for k in y_counter:
                    if k in x_counter:
                        re = 0
                        break
                if re != 0:
                    res = max(res, le * re)
                    max_re = re
        return res


sol = Solution()
print(sol.maxProduct(["a","aa","aaa","aaaa"]))