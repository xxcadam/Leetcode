import collections
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time_branch = []
        # {managerId: employeeId}
        managerDic = collections.defaultdict(list)

        for i, e in enumerate(manager):
            managerDic[e].append(i)

        self.bp(headID, time_branch, managerDic, informTime, 0)

        return max(time_branch)

    def bp(self, id, time_branch, managerDic, informTime, beforTime):
        if informTime[id] == 0:
            time_branch.append(beforTime)
        else:
            for eid in managerDic[id]:
                self.bp(eid, time_branch, managerDic, informTime, beforTime + informTime[id])

        # return time_branch


solution = Solution()

print(solution.numOfMinutes(6, 2, [2, 2,-1,2,2,2], [0,0,1,0,0,0]))