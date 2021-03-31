class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            if row[0] > target:
                break
            if row[0] == target or row[-1] == target:
                return True
            elif row[0] < target <row[-1]:
                for x in row:
                    if x == target:
                        return True
                    elif x > target:
                        break
            
        return False
