from collections import Counter
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def smallest_Count(str):
            x = Counter(str)
            for i in range(97, 123):
                if x[chr(i)] != 0:
                    return x[chr(i)]
        words_f = []
        for word in words:
            words_f.append(smallest_Count(word))
        res = []
        for query in queries:
            cnt = smallest_Count(query)

            res.append(sum([i > cnt for i in words_f ]))
        return res


sol = Solution()
print(sol.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))


