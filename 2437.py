class Solution:
    def countTime(self, time: str) -> int:
        if "?" not in time:
            return 0
        hr = time[:2]
        mi = time[-2:]
        if "?" not in hr:
            h_fac = 1
        elif hr == "??":
            h_fac = 24
        elif hr[0] == "?":
            if int(hr[1]) >3:
                h_fac = 2
            else:
                h_fac = 3
        elif hr[1] == "?":
            if int(hr[0]) == 2:
                h_fac = 4
            else:
                h_fac = 10
        else:
            h_fac = 10

        if "?" not in mi:
            min_fac = 1
        elif mi == "??":
            min_fac = 60
        elif mi[0] == "?":
            min_fac = 6
        else:
            min_fac = 10


        return min_fac * h_fac



sol = Solution()
print(sol.countTime("07:?3"))