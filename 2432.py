from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        worker, maxCost = logs[0]
        for i in range(1, len(logs)):
            idc = logs[i][0]
            time = logs[i][1] - logs[i - 1][1]

            if time > maxCost or (time == maxCost and idc < worker):
                worker = idc
                maxCost = time

        return worker

sol = Solution()
print(sol.hardestWorker(10,
[[0,3],[2,5],[0,9],[1,15]]))