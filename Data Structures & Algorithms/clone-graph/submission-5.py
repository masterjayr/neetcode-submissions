"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {None:None}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]


            newNode = Node(node.val)
            oldToNew[node] = newNode
            for i in node.neighbors:
                oldToNew[node].neighbors.append(clone(i))

            return newNode

        return clone(node)
        

