from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return not(event1[1] < event2[0] or event2[1] < event1[0])


sol = Solution()
print(sol.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]))