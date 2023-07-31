class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 != 0:
            return -1
        c, r, o, a, k = 0, 0, 0, 0, 0
        free_frog = 0
        frog = 0
        for h in croakOfFrogs:
            if h == "c":
                c += 1
                if free_frog > 0:
                    free_frog -= 1
                else:
                    frog += 1
            elif h == "r":
                if c > 0:
                    c -= 1
                    r += 1
                else:
                    return - 1
            elif h == "o":
                if r > 0:
                    r -= 1
                    o += 1
                else:
                    return - 1
            elif h == "a":
                if o > 0:
                    o -= 1
                    a += 1
                else:
                    return - 1
            elif h == "k":
                if a > 0:
                    a -= 1
                    free_frog += 1
                else:
                    return -1

        return frog if c + r + o + a + k == 0 else -1


sol = Solution()
print(sol.minNumberOfFrogs("croakcroak"))
assert sol.minNumberOfFrogs("croakcroak") == 1
assert sol.minNumberOfFrogs("crocracokrakoak") == 3
assert sol.minNumberOfFrogs("crocakcroraoakk") == 2