# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # so [1, 2, N, N, 3, 4, N, N, 5, N, N] -> encode in preorder
        res = []

        def preorder(root):
            if not root:
                res.append("N")
                return 

            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return " ".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(" ")
        self.i = 0
        def dfs():  
            if self.i == len(values):
                return
            if values[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()







