# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(root, lastVal):

            if not root:
                return 0

            res = 1 if root.val >= lastVal else 0
            res += dfs(root.left, max(lastVal, root.val))
            res += dfs(root.right, max(lastVal, root.val))

            return res

        return dfs(root, root.val)
