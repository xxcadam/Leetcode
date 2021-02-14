class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        if j <  1:
            return 0
        maxarea = 0
        while i < j:
            if height[i] <= height[j]:
               area = (j - i)*height[i]
               i = i + 1
            else:
                area = (j - i)*height[j]
                j = j - 1
            if area > maxarea:
                maxarea = area
        
        return maxarea
