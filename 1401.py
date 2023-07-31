import math


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        val = radius ** 2 - (x1 - xCenter) ** 2
        if val >= 0:
            # has cross for this value
            new_y1 = math.sqrt(val) + yCenter
            new_y2 = -math.sqrt(val) + yCenter
            if y1 <= new_y1 <= y2 or y1 <= new_y2 <= y2 or new_y2 <= y1 <= new_y2 or new_y2 <= y2 <= new_y1:
                return True

        val = radius ** 2 - (x2 - xCenter) ** 2
        if val >= 0:
            # has cross for this value
            new_y1 = math.sqrt(val) + yCenter
            new_y2 = -math.sqrt(val) + yCenter
            if y1 <= new_y1 <= y2 or y1 <= new_y2 <= y2 or new_y2 <= y1 <= new_y2 or new_y2 <= y2 <= new_y1:
                return True

        val = radius ** 2 - (y1 - yCenter) ** 2
        if val >= 0:
            # has cross for this value
            new_x1 = math.sqrt(val) + xCenter
            new_x2 = -math.sqrt(val) + xCenter
            if x1 <= new_x1 <= x2 or x1 <= new_x2 <= x2 or new_x1 <= x1 <= new_x2 or new_x1 <= x2 <= new_x2:
                return True
        val = radius ** 2 - (y2 - yCenter) ** 2
        if val >= 0:
            # has cross for this value
            new_x1 = math.sqrt(val) + xCenter
            new_x2 = -math.sqrt(val) + xCenter
            if x1 <= new_x1 <= x2 or x1 <= new_x2 <= x2 or new_x1 <= x1 <= new_x2 or new_x1 <= x2 <= new_x2:
                return True
        return False


sol = Solution()
print(sol.checkOverlap(radius=18, xCenter=11, yCenter=19, x1=7, y1=12, x2=10, y2=20))


