# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional



class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root:
            return None

        def dfs(node, height):
            height1 = height
            height2 = height
            val = node.val
            val2 = node.val
            if node.left:
                val, height1 = dfs(node.left, height + 1)
            if node.right:
                val2, height2 = dfs(node.right, height + 1)
            if height1 >= height2:
                return val, height1
            else:
                return val2, height2

        return dfs(root, 0)[0]
