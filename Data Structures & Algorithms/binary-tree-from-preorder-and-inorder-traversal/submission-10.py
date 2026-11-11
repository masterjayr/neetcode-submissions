# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {v : i for i, v in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(l, r):
            if l > r: return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            index = indices[root_val]
            node = TreeNode(root_val)
            node.left = dfs(l, index-1)
            node.right = dfs(index+1, r)

            return node

        return dfs(0, len(inorder) - 1)