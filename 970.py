from typing import List
from math import log


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        if x == 1 and y != 1:
            res = [2]
            tmp = y ** x + 1
            while tmp <= bound:
                res.append(tmp)
                x += 1
                tmp = y ** x + 1
            return res
        elif y == 1 and x != 1:
            x, y = y, x
            res = [2]
            tmp = y ** x + 1
            while tmp <= bound:
                res.append(tmp)
                x += 1
                tmp = y ** x + 1
            return res
        elif x == 1 and y == 1:
            if bound >= 2:
                return [2]
            return []

        res = set()
        log_x = int(log(bound, x)) + 1
        log_y = int(log(bound, y)) + 1
        for i in range(log_x):
            for j in range(log_y):
                tmp = x ** i + y ** j
                if tmp <= bound:
                    res.add(tmp)
                else:
                    break

        return list(res)


solution = Solution()
print(solution.powerfulIntegers(x=2, y=3, bound=0))
