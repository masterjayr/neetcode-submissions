# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):

            if not root:
                return [0, True]

            
            left = helper(root.left)
            right = helper(root.right)
            isBalanced = abs(left[0] - right[0]) < 2 and left[1] and right[1]

            return [1 + max(left[0], right[0]), isBalanced]

        return helper(root)[1]
