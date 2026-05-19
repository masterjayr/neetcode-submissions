# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        def dfs(node, maxValue):

            if not node:
                return 0

            res = (1 if node.val >= maxValue else 0)
            newMax = max(maxValue, node.val)
            res += dfs(node.left, newMax)
            res += dfs(node.right, newMax)

            return res

        return dfs(root, root.val)
